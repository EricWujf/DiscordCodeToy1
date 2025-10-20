# 自製小玩具 V1.1.1
import os #引入 os 套件
import yaml #引入 yaml 套件

# 程式所在目錄
BASEDIR = os.path.dirname(os.path.abspath(__file__))
# 建立輸出目錄
OUTPUTDIR = os.path.join(BASEDIR, "Output")
os.makedirs(OUTPUTDIR, exist_ok=True)
# 讀取設定檔
config_path = os.path.join(BASEDIR, 'config.yml')

with open(os.path.join(OUTPUTDIR, "output.txt"), "w", encoding="utf-8") as f: #清空程式輸出檔案
            f.write("")

try:
    with open(config_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        loop_limit = data['CodeToy']['LoopLimit']
        debug_mode = data['CodeToy']['DebugMode']
    with open(os.path.join(OUTPUTDIR, "BugReport.txt"), "w", encoding="utf-8") as f: #程式輸出檔案
            f.write(f"尚未發現錯誤\n")
except yaml.YAMLError as e:
    print(f'解析 YAML 時發生錯誤: {e}')
    loop_limit = 50  # 預設值
    with open(os.path.join(OUTPUTDIR, "BugReport.txt"), "w", encoding="utf-8") as f: #程式輸出檔案
            f.write(f"解析 YAML 時發生錯誤: {e}\n")
except FileNotFoundError:
    print('找不到檔案，使用預設值')
    loop_limit = 50  # 預設值
    with open(os.path.join(OUTPUTDIR, "BugReport.txt"), "w", encoding="utf-8") as f: #程式輸出檔案
            f.write("找不到檔案\n")

if debug_mode == 1:
    with open(os.path.join(BASEDIR, "DeBug.txt"), "w", encoding="utf-8") as f: #程式輸出檔案
            f.write(f"---------- 除錯模式 : 開啟 ----------\n")
            f.write(f"程式所在目錄: {BASEDIR}\n")
            f.write(f"輸出目錄: {OUTPUTDIR}\n")
            f.write(f"設定檔路徑: {config_path}\n")
else:
    if os.path.exists(os.path.join(BASEDIR, "DeBug.txt")):
        os.remove(os.path.join(BASEDIR, "DeBug.txt"))
    
# 主程式
i = 0 #計數器
limit = loop_limit*2 #計算最大循環次數
while i < limit:
    i += 1
    if i%2 == 1:
        print("掛滿")
        with open(os.path.join(OUTPUTDIR, "output.txt"), "a", encoding="utf-8") as f: #輸出檔案
            f.write("掛滿\n")
    elif i%2 == 0:
        print("炸服")
        with open(os.path.join(OUTPUTDIR, "output.txt"), "a", encoding="utf-8") as f: #輸出檔案
            f.write("炸服\n")