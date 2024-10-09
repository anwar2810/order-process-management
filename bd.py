def main():
    # 設置變數
    file_path = "D:/github/iss-a.xlsx"
    sheet_name = "Sheet1"
    output_file = "D:/github/_sample.xlsx"
    
    # 呼叫處理函數
    process_excel(file_path, sheet_name, output_file)

# 呼叫主函數
if __name__ == "__main__":
    main()
