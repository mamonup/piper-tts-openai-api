1. Grab piper_windows_amd64.zip from rhasspy/piper and extract (tested with rhasspy/piper release 2023.11.14-2)
2. Put app_simple.py in the same folder as piper.exe (extracted in step 1)
3. Create a 'piper_models' folder in the same 
4. Place your .onnx piper TTS voice file and .onnx.json file inside 'piper_models'
5. Make sure your .onnx.json file has the same name as your .onnx voice file (.onnx.json file is REQUIRED)
6. Edit 'REPLACE_MODEL_HERE.onnx' in app_simple.py with your .onnx piper TTS voice file's exact name
7. Run app_simple.py

For Open WebUI:
1. Use http://localhost:5002/v1 as the API Base URL
2. Place anything in the API Key (API Key cannot be blank)
3. Place anything in TTS Voice
4. Place anything in TTS Model

Tested working with Open WebUI v0.3.32

Possible todo:
sysarg for .onnx voice file
error checking
validation
