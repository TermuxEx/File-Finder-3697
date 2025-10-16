# File Finder 3697

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey.svg)

## 🔍 Advanced Archive Password Recovery Tool

**File Finder 3697** is a powerful password recovery tool designed for **authorized penetration testing**, **digital forensics**, and **educational purposes**. This tool specializes in cracking passwords for various archive formats including ZIP, RAR, 7Z, and PDF files using dictionary-based brute force attacks.

Created by **Admin. Umar Ruman**, File Finder 3697 incorporates advanced password testing techniques to recover access to protected archives with real-time feedback and comprehensive logging.

## ⚠️ DISCLAIMER

This tool is intended for **authorized security testing and educational purposes only**. By using this tool, you agree that:
1. You have explicit written permission to test the systems involved
2. You will only use this tool on systems you are authorized to access
3. You will comply with all applicable local, state, and federal laws
4. You will not use this tool for any malicious or unauthorized activities

**Unauthorized use is strictly prohibited and may result in criminal charges.**

## 🌟 Features

- **Multi-Format Archive Support**: Handles ZIP, RAR, 7Z, and PDF files
- **Dictionary Attack**: Uses wordlist-based password testing
- **Real-Time Feedback**: Shows current password being tested
- **Progress Tracking**: Displays testing progress and statistics
- **Colored Output**: Enhanced visual feedback with color-coded results
- **Detailed Logging**: Comprehensive logging for forensic purposes
- **Automatic Result Saving**: Saves found passwords to `cracked_passwords.txt`
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Rate Monitoring**: Shows password testing rate per second

## 📋 Requirements

- Python 3.6 or higher
- rarfile library
- pyminizip library
- PyPDF2 library (for PDF support)

## 🔧 Installation

### Method 1: Direct Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/File-Finder-3697.git
cd File-Finder-3697

# Install required packages
pip install -r requirements.txt
```

### Method 2: Manual Installation
```bash
# Install dependencies
pip install rarfile pyminizip PyPDF2

# Download the script
wget https://raw.githubusercontent.com/yourusername/File-Finder-3697/main/file_finder_3697.py
```

### Requirements File (requirements.txt)
```txt
rarfile>=4.0
pyminizip>=0.2.4
PyPDF2>=1.26.0
```

## 🚀 Usage

### Basic Usage
```bash
python file_finder_3697.py
```

The tool will guide you through the process interactively:
1. Authorization confirmation
2. Target file path entry
3. Wordlist file path entry
4. Password testing process
5. Results display

### Prerequisites

You need:
1. A password-protected archive file (ZIP, RAR, 7Z, or PDF)
2. A wordlist file containing potential passwords (one per line)

## 📖 How It Works

### Password Testing Process:
1. **Authorization Check**: Confirms legitimate usage
2. **File Validation**: Verifies target file exists and is supported
3. **Wordlist Loading**: Reads passwords from provided wordlist
4. **Sequential Testing**: Tests each password in the wordlist
5. **Real-Time Feedback**: Shows current password being tested
6. **Validation**: Attempts to open/archive with each password
7. **Result Recording**: Saves successful passwords to file

### Supported Formats:
- **ZIP Files**: Uses built-in zipfile library
- **RAR Files**: Uses rarfile library
- **PDF Files**: Uses PyPDF2 library
- **7Z Files**: Partial support (requires py7zr for full functionality)

### Security Features:
- **Rate Limiting**: Prevents resource exhaustion
- **Error Handling**: Graceful handling of invalid passwords
- **Interrupt Support**: Clean exit on Ctrl+C
- **Logging**: Detailed activity logging for audit purposes

## 📚 Usage Examples

### Example 1: Crack a ZIP file
```bash
python file_finder_3697.py
# Enter: /path/to/protected.zip
# Enter: /path/to/wordlist.txt
```

### Example 2: Crack a RAR file
```bash
python file_finder_3697.py
# Enter: /path/to/protected.rar
# Enter: /path/to/password_list.txt
```

### Example 3: Crack a PDF file
```bash
python file_finder_3697.py
# Enter: /path/to/protected.pdf
# Enter: /path/to/dictionary.txt
```

## ⚙️ Configuration

### Wordlist Format
Create a text file with one password per line:
```
password123
admin123
letmein
qwerty
password
123456
```

### Output Files
- `finder_detailed.log`: Detailed activity log
- `cracked_passwords.txt`: Successful password results

## 🛠️ Troubleshooting

### Common Issues:
1. **"Module not found" errors**:
   - Install required packages: `pip install rarfile pyminizip PyPDF2`
   
2. **"File not found"**:
   - Check file paths for typos
   - Ensure proper file permissions
   - Use absolute paths if relative paths fail

3. **"Unsupported file format"**:
   - Current version supports: .zip, .rar, .7z, .pdf
   - For 7Z full support, install py7zr: `pip install py7zr`

### Performance Tips:
- Use focused, targeted wordlists for faster results
- Sort wordlists by likelihood (common passwords first)
- Monitor system resources during long operations
- Use SSD storage for better I/O performance

## 🔒 Security Considerations

This tool is for LEGITIMATE SECURITY RESEARCH ONLY!

### Best Practices
1. Only test files you own or have explicit permission to test
2. Maintain detailed logs of all testing activities
3. Store wordlists securely and appropriately
4. Report findings through proper channels
5. Keep software and libraries updated

## 📄 Legal and Ethical Usage

**This tool is for LEGITIMATE SECURITY RESEARCH ONLY!**

Before using this tool, ensure you have:
1. Written authorization from system owners
2. Defined scope of testing activities
3. Proper documentation of all actions
4. Clear understanding of applicable laws

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

### Areas for Improvement:
- Add support for additional archive formats
- Implement brute-force mode alongside dictionary attacks
- Add GUI interface for easier usage
- Improve performance optimization
- Add proxy support for distributed testing

## 📞 Contact

For questions about legitimate security research usage:
- YouTube: [Cyber Ex Study](https://youtube.com)
- Instagram: [@cyberex3697](https://instagram.com)
- GitHub: [https://github.com/CyberEx3697](https://github.com/CyberEx3697)

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Final Note

This tool is provided for educational and authorized security testing purposes. The creator assumes no liability for misuse. Always follow ethical guidelines and legal requirements in your security research activities.

Remember that password cracking can be time-intensive. Complex passwords with large wordlists may take hours or days to process. Always test within authorized timeframes and scopes.

---
**Remember**: With great power comes great responsibility. Use this tool ethically and legally!
