def average(*marks):
    total=sum(marks)
    count=len(marks)
    return total/count
if __name__=="__main__":
        print(average(80,90,95))