## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate virtual environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up database

```bash
python.exe .\setup\setupDatabase.py
``` 

### 5. Import data via openligadb API
python.exe .\api\fetchData.py