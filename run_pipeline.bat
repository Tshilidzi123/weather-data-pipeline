@echo off
echo Running Weather Data Pipeline...
cd C:\Users\tshilidzi.maphiri\weather_data_pipeline
"C:\Users\tshilidzi.maphiri\AppData\Local\Programs\Python\Python310\python.exe" scripts\extract_data.py
"C:\Users\tshilidzi.maphiri\AppData\Local\Programs\Python\Python310\python.exe" scripts\transform_data.py
"C:\Users\tshilidzi.maphiri\AppData\Local\Programs\Python\Python310\python.exe" scripts\load_to_mysql.py
echo  Pipeline complete!
pause
