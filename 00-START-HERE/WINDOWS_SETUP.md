# Windows 11 (64-bit) Setup

## Install free tools from official sources
- Git for Windows: https://git-scm.com/download/win
- Visual Studio Code: https://code.visualstudio.com/
- Python: https://www.python.org/downloads/windows/
- Power BI Desktop: https://powerbi.microsoft.com/desktop/
- SQLite: https://sqlite.org/download.html
- LibreOffice (optional): https://www.libreoffice.org/

## Verify in PowerShell
```powershell
git --version
python --version
py --version
code --version
```

## Clone the repository
```powershell
gh auth login
gh repo clone 596555/pharmaintelligence
cd pharmaintelligence
code .
```
Without GitHub CLI:
```powershell
git clone https://github.com/596555/pharmaintelligence.git
cd pharmaintelligence
code .
```

## Create a Python environment
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pandas matplotlib jupyter pytest
```
If PowerShell blocks activation, use Command Prompt:
```cmd
.venv\Scripts\activate.bat
```

## Free learning platforms
- Google Colab: https://colab.research.google.com/
- Kaggle Learn: https://www.kaggle.com/learn
- SQLBolt: https://sqlbolt.com/
- Microsoft Learn: https://learn.microsoft.com/training/

Power BI/local Python performance depends on RAM and CPU. Use small datasets or Colab if needed.
