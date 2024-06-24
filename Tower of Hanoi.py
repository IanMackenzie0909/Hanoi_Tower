'''
    正常版河內塔
    規則: 有三根杆子A，B，C。
          A 杆上有 N 個圓盤，圓盤由小到大編號為 1 到 N。
          要求按下列規則將所有圓盤移至 C 杆：
          
          1. 每次只能移動一個圓盤
          2. 大盤不能疊在小盤上面
          
    ※ A桿(start) B桿(middle) C桿(destination)
'''

n = int(input('請輸入正整數:'))

def towers(n, start, destination , middle):
    
  if n > 0:
    # 將n-1個盤子從A移動到B，C作為輔助的柱子
    towers(n - 1, start, middle, destination )

    # 將第n個盤子從A移動到C
    print(f"{n} 號原盤 : {start}-->{destination}")

    # 將n-1個盤子從B移動到C，利用A作為輔助柱子
    towers(n - 1, middle, destination, start)

# 呼叫函式
towers(n, 'A', 'C', 'B')