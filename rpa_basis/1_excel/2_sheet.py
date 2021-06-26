from openpyxl import Workbook
wb=Workbook()
# wb.active
ws=wb.create_sheet() # 새로운 sheet 기본 이름으로 생성
ws.title="Mysheet" #sheet명 변경
ws.sheet_properties.tabcolor = "ff66ff" # RGB 형태로 값을 넣어주면 탭 색상 변경, 구글링해서 색상표 확인

ws1=wb.active_sheet("Yoursheet") #주어진 이름으로 Sheet 생성
ws1=wb.active_sheet("Newsheet", 2) #2번째 index에 sheet 생성 

new_ws=wb["Newsheet"] # Dict 형태로 Sheet 에 접근

wb.save("sample.xlsx")