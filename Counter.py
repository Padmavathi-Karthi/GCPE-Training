# your first while loop: can you guess what it does?

limit = 120

counter = 1
while counter < limit:
    if counter > 10:
        break
    else:
        print(counter)
    counter = counter + 1
    # print("Finished")   # it will print in each and every lines.
    
print("Finished")   # it will print only if the condition is not satisfied