#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
███████╗██╗██╗     ███████╗╗
██╔════╝██║██║     ██╔════╝╝
█████╗  ██║██║     █████╗
██╔══╝  ██║██║     ██╔══╝
██║     ██║███████╗███████╗
╚═╝     ╚═╝╚══════╝╚══════╝╝
                                                                      
                ╚═╝      ╚═════╝  ╚═════╝    ╚═╝   ╚══════╝
                                                                      
                     Version: 1.0
                     Author: Admin. Umar Ruman
"""

import os
import sys
import time
import zipfile
import rarfile
import tarfile
import logging
from pathlib import Path
from getpass import getpass
import pyminizip
import hashlib

class FileFinder3697:
    def __init__(self):
        self.tool_name = "File Finder 3697"
        self.version = "1.0"
        self.author = "Admin. Umar Ruman"
        self.supported_formats = ['.zip', '.rar', '.7z', '.tar', '.tar.gz', '.pdf']
        self.found_password = None
        
        # Setup logging
        logging.basicConfig(
            filename='finder_detailed.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_block_text(self):
        """Print decorative block text"""
        block_art = """
###############################################################################
###############################################################################

        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697
        3697                                                    3697

                █████╗ ██████╗ ██╗██╗     ███████╗██████╗ 
                ██╔══██╗██╔══██╗██║██║     ██╔════╝██╔══██╗
                ███████║██████╔╝██║██║     █████╗  ██║  ██║
                ██╔══██║██╔══██╗██║██║     ██╔══╝  ██║  ██║
                ██║  ██║██████╔╝██║███████╗███████╗██████╔╝
                ╚═╝  ╚═╝╚═════╝ ╚═╝╚══════╝╚══════╝╚═════╝ 

###############################################################################
###############################################################################
                          A d m i n . U m a r   R u m a n
                    
###############################################################################
###############################################################################
        """
        print(block_art)
    
    def print_intro(self):
        """Print tool introduction"""
        intro_text = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                    TOOL INFO                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  Tool: File Finder 3697                                                     ║
║  Version: {self.version:<51} ║
║  Author: {self.author:<52} ║
║                                                                              ║
║  [ ★ ] Description:                                                         ║
║      Professional password brute-force tool for archived files              ║
║      Capable of cracking password-protected ZIP, RAR, 7Z & PDF files         ║
║                                                                              ║
║  [ ★ ] Features:                                                            ║
║      ┌─ Multi-format support (.zip, .rar, .7z, .pdf)                        ║
║      ┌─ Real-time password testing display                                  ║
║      ┌─ Colored output for clear results                                    ║
║      ┌─ Detailed logging for forensic purposes                              ║
║      ┌─ Automatic result saving                                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(intro_text)
    
    def print_disclaimer(self):
        """Print legal disclaimer"""
        disclaimer = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                           L E G A L   D I S C L A I M E R                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  [ ! ] ETHICAL USAGE WARNING                                                 ║
║      This tool is designed for EDUCATIONAL PURPOSES ONLY.                    ║
║      Unauthorized usage against files you don't own is ILLEGAL.              ║
║                                                                              ║
║  [ ! ] LEGAL REQUIREMENTS                                                    ║
║      ▓ You MUST have EXPLICIT WRITTEN PERMISSION from the file owner         ║
║      ▓ Testing must be within agreed scope and timeframe                     ║
║      ▓ All findings must be reported responsibly                             ║
║      ▓ Any damage caused by misuse is YOUR RESPONSIBILITY                    ║
║                                                                              ║
║  [ ! ] AUTHOR DISCLAIMERS                                                    ║
║      Admin. Umar Ruman DISCLAIMS ALL LIABILITY for unauthorized use.         ║
║      By using this tool, you ACKNOWLEDGE full responsibility for actions.    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
        """
        print(disclaimer)
    
    def print_colored(self, text, color="white"):
        """Print colored text"""
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "purple": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        print(f"{colors.get(color, colors['white'])}{text}{colors['reset']}")
    
    def authorization_check(self):
        """Check if user is authorized"""
        print("\n")
        self.print_colored("[?] Are you using this tool for AUTHORIZED work? (y/n): ", "cyan")
        choice = input().strip().lower()
        
        if choice not in ['y', 'yes']:
            self.print_colored("[*] Nice try babe, but it's your bad luck :)", "red")
            self.print_colored("[*] Exiting tool safely...", "red")
            time.sleep(2)
            return False
        return True
    
    def get_file_path(self):
        """Get target file path from user"""
        while True:
            self.print_colored("\n[?] Enter path to password-protected file: ", "cyan")
            file_path = input().strip().replace('"', '').replace("'", "")
            
            if not os.path.exists(file_path):
                self.print_colored("[!] File not found. Please try again.", "red")
                continue
                
            if not os.path.isfile(file_path):
                self.print_colored("[!] Path is not a file. Please try again.", "red")
                continue
                
            file_ext = Path(file_path).suffix.lower()
            if file_ext not in self.supported_formats:
                supported = ', '.join(self.supported_formats)
                self.print_colored(f"[!] Unsupported file format. Supported: {supported}", "red")
                continue
                
            return file_path, file_ext
    
    def get_wordlist_path(self):
        """Get wordlist file path from user"""
        while True:
            self.print_colored("[?] Enter path to password wordlist file: ", "cyan")
            wordlist_path = input().strip().replace('"', '').replace("'", "")
            
            if not os.path.exists(wordlist_path):
                self.print_colored("[!] Wordlist file not found. Please try again.", "red")
                continue
                
            if not os.path.isfile(wordlist_path):
                self.print_colored("[!] Path is not a file. Please try again.", "red")
                continue
                
            return wordlist_path
    
    def read_wordlist(self, wordlist_path):
        """Read passwords from wordlist"""
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                passwords = [line.strip() for line in f if line.strip()]
                if not passwords:
                    self.print_colored("[!] Wordlist is empty!", "red")
                    return []
                return passwords
        except Exception as e:
            self.print_colored(f"[!] Error reading wordlist: {e}", "red")
            return []
    
    def test_zip_password(self, file_path, password):
        """Test password for ZIP file"""
        try:
            with zipfile.ZipFile(file_path, 'r') as zip_file:
                zip_file.setpassword(password.encode())
                # Try to read first file to verify password
                first_file = zip_file.namelist()[0] if zip_file.namelist() else None
                if first_file:
                    zip_file.read(first_file)
                return True
        except:
            return False
    
    def test_rar_password(self, file_path, password):
        """Test password for RAR file"""
        try:
            with rarfile.RarFile(file_path, 'r') as rar_file:
                rar_file.setpassword(password)
                # Try to read first file to verify password
                first_file = rar_file.namelist()[0] if rar_file.namelist() else None
                if first_file:
                    rar_file.read(first_file)
                return True
        except:
            return False
    
    def test_pdf_password(self, file_path, password):
        """Test password for PDF file"""
        try:
            import PyPDF2
            with open(file_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                if reader.is_encrypted:
                    return reader.decrypt(password) == 1
            return False
        except ImportError:
            self.print_colored("[!] PyPDF2 module required for PDF cracking", "red")
            return False
        except:
            return False
    
    def crack_file_password(self, file_path, file_ext, passwords):
        """Perform brute force attack on password-protected file"""
        self.print_colored(f"\n[*] Starting brute force attack on: {os.path.basename(file_path)}", "cyan")
        self.print_colored(f"[*] Testing {len(passwords)} passwords...\n", "cyan")
        
        tested_count = 0
        start_time = time.time()
        
        try:
            for i, password in enumerate(passwords):
                tested_count = i + 1
                password_display = password[:20] + "..." if len(password) > 20 else password
                
                # Display current password being tested
                self.print_colored(f"[→] Trying password: {password_display}", "white")
                
                # Test password based on file type
                is_valid = False
                try:
                    if file_ext == '.zip':
                        is_valid = self.test_zip_password(file_path, password)
                    elif file_ext == '.rar':
                        is_valid = self.test_rar_password(file_path, password)
                    elif file_ext in ['.pdf']:
                        is_valid = self.test_pdf_password(file_path, password)
                    # Note: 7Z support requires py7zr library
                except Exception as e:
                    logging.debug(f"Password test error: {e}")
                    is_valid = False
                
                # Show result
                if is_valid:
                    self.print_colored(f"[★] PASSWORD FOUND: {password}", "yellow")
                    self.found_password = password
                    # Save result
                    with open('cracked_passwords.txt', 'a') as f:
                        f.write(f"{file_path}:{password}\n")
                    logging.info(f"PASSWORD FOUND for {file_path}: {password}")
                    return True
                else:
                    self.print_colored(f"[-] Password '{password_display}' - FAILED", "red")
                
                # Show progress
                if tested_count % 10 == 0:
                    elapsed = time.time() - start_time
                    rate = tested_count / elapsed if elapsed > 0 else 0
                    self.print_colored(f"[{tested_count}/{len(passwords)}] Completed @ {rate:.1f} passwords/sec", "blue")
                
                # Small delay to prevent resource exhaustion
                time.sleep(0.01)
                
        except KeyboardInterrupt:
            self.print_colored("\n[!] Attack interrupted by user", "red")
            elapsed = time.time() - start_time
            self.print_colored(f"[*] Tested {tested_count} passwords in {elapsed:.2f} seconds", "blue")
            return False
        
        # Attack completed without finding password
        elapsed = time.time() - start_time
        self.print_colored(f"\n[*] Attack completed in {elapsed:.2f} seconds", "blue")
        self.print_colored(f"[*] Tested {tested_count} passwords", "blue")
        self.print_colored("[*] No valid password found", "red")
        return False
    
    def show_final_message(self):
        """Show final message with social links"""
        print("\n" + "="*80)
        self.print_colored("THANK YOU FOR USING FILE FINDER 3697!", "green")
        print("="*80)
        self.print_colored("For more professional security tools, visit:", "cyan")
        self.print_colored("  • YouTube: Cyber Ex Study", "white")
        self.print_colored("  • Instagram: @cyberex3697", "white")
        self.print_colored("  • GitHub: https://github.com/CyberEx3697", "white")
        print("="*80)
    
    def run(self):
        """Main execution method"""
        try:
            # Show welcome screen
            self.clear_screen()
            self.print_block_text()
            self.print_intro()
            self.print_disclaimer()
            
            # Authorization check
            if not self.authorization_check():
                return
            
            # Get file and wordlist paths
            file_path, file_ext = self.get_file_path()
            wordlist_path = self.get_wordlist_path()
            
            # Load wordlist
            passwords = self.read_wordlist(wordlist_path)
            if not passwords:
                return
            
            # Perform cracking
            success = self.crack_file_password(file_path, file_ext, passwords)
            
            # Show final results
            if success:
                self.print_colored(f"\n[★] SUCCESS: Password cracked for {os.path.basename(file_path)}", "green")
                self.print_colored(f"[★] Found password: {self.found_password}", "yellow")
            else:
                self.print_colored(f"\n[!] FAILED: Could not crack {os.path.basename(file_path)}", "red")
                self.print_colored("[!] Remember: False negatives are common. Consider alternate strategies.", "red")
            
            # Show final message
            self.show_final_message()
            
        except KeyboardInterrupt:
            self.print_colored("\n\n[*] Tool terminated by user", "red")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            self.print_colored(f"\n[!] Unexpected error occurred: {e}", "red")

def main():
    tool = FileFinder3697()
    tool.run()

if __name__ == "__main__":
    main()
