import glob
import os
import re

def analyze_logs():
    # Find all server*.log files in the current directory
    log_files = sorted(glob.glob("server*.log"))
    
    if not log_files:
        print("No server*.log files found in the current directory.")
        return
    
    print("=" * 65)
    print(f"{'Server':<12} | {'CRC Error (Errors Only)':<22} | {'Link Down (Errors Only)':<22}")
    print("-" * 65)
    
    results = {}
    
    for file_path in log_files:
        # Extract server name (e.g., server01) from filename
        server_name = os.path.basename(file_path).split('.')[0]
        
        crc_errors = 0
        link_down_errors = 0
        
        # We will also count literal occurrences (including INFO/recovery lines) for complete transparency
        crc_literal = 0
        link_down_literal = 0
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line_lower = line.lower()
                
                # Check for the error patterns
                has_crc = bool(re.search(r'crc\s+error', line_lower))
                has_link_down = bool(re.search(r'link\s+down', line_lower))
                
                # Check if this line is an ERROR-level log
                is_error = "ERROR" in line
                
                if has_crc:
                    crc_literal += 1
                    if is_error:
                        crc_errors += 1
                        
                if has_link_down:
                    link_down_literal += 1
                    if is_error:
                        link_down_errors += 1
                        
        results[server_name] = {
            'crc_errors': crc_errors,
            'link_down_errors': link_down_errors,
            'crc_literal': crc_literal,
            'link_down_literal': link_down_literal
        }
        
        print(f"{server_name:<12} | {crc_errors:<22} | {link_down_errors:<22}")
        
    print("=" * 65)
    print("\n* Detailed breakdown (including literal substring counts vs. actual ERROR events):")
    for server, data in results.items():
        print(f"\n[{server}]")
        print(f"  - CRC Error occurrences:")
        print(f"    * Actual ERROR Logs: {data['crc_errors']}")
        print(f"    * Total Substring Matches (including INFO/recovery/checks): {data['crc_literal']}")
        print(f"  - Link Down occurrences:")
        print(f"    * Actual ERROR Logs: {data['link_down_errors']}")
        print(f"    * Total Substring Matches: {data['link_down_literal']}")
    print("=" * 65)

if __name__ == "__main__":
    analyze_logs()
