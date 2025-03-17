import os
import pandas as pd
import subprocess

# 設定路徑與參數
detect_script = 'detect_dual.py'  
weights_path = '20250205.pt'  
video_path = 'V2.mp4' 
output_folder = './runs/detect/' 

# Step 1: 執行 detect.py 並產生檢測結果
command = f'python {detect_script} --source "{video_path}" --weights "{weights_path}" --img 640 --save-txt --name 20250215'
subprocess.run(command, shell=True)

# Step 2: 讀取 detect.py 產生的 .txt 檔案，並整理成 DataFrame
output_path = os.path.join(output_folder, 'detection_output', 'labels')
results_list = []

for txt_file in os.listdir(output_path):
    frame_number = int(os.path.splitext(txt_file)[0])  
    with open(os.path.join(output_path, txt_file), 'r') as f:
        for line in f:
            data = line.strip().split()
            cls, x_center, y_center, width, height = map(float, data[:5])
            results_list.append({
                "Frame": frame_number,
                "Class": int(cls),
                "x_center": round(x_center, 4),
                "y_center": round(y_center, 4),
                "Width (normalized)": round(width, 4),
                "Height (normalized)": round(height, 4)
            })

# Step 3: 保存為 Excel 檔案
df = pd.DataFrame(results_list)
df.to_excel('detection_results_from_detect.xlsx', index=False)
print("檢測結果已保存為 detection_results_from_detect.xlsx")






#def txt_to_excel(folder_path, output_excel):
 #   data = []
  #  
   # # 讀取資料夾內所有 .txt 檔案
    #for file_name in os.listdir(folder_path):
     #   if file_name.endswith(".txt"):
      #      file_path = os.path.join(folder_path, file_name)
       #     
        #    with open(file_path, 'r', encoding='utf-8') as file:
         #       content = file.read()
          #      data.append([file_name, content])
    
    # 建立 DataFrame
   # df = pd.DataFrame(data, columns=['File Name', 'Content'])
    
    # 儲存到 Excel
   # df.to_excel(output_excel, index=False, engine='openpyxl')
    #print(f"Excel 檔案已儲存至 {output_excel}")

#folder_path = "runs/detect/20250215/labels" 
#output_excel = folder_path+"202520250217"  
#txt_to_excel(folder_path, output_excel)

