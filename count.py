def main():
  array = []
  num = int(input("enter start number\n"))

  for i in range(10):
    array.append([])
    for j in range(20):
      array[i].append(num)
      if(i > 4):
        num -= 1
      else:
        num += 1
    print(array[i])

if(__name__ == '__main__'):
  main()
