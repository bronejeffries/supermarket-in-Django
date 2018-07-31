from cashier.models import Products
import csv

def addnewitem(name,selling_price,available_quantity=0):
            newItem = Products()
            newItem.name = name
            newItem.selling_price= selling_price
            newItem.available_quantity = available_quantity
            try:
                newItem.save()
            except Exception as e:
                return False
            else:
                return True

def handle_uploaded_file(uploadf):
        #reader = csv.reader(uploadf)

        #write into a new file that will be used for extraction
        with open('newitemslist.csv','wb+') as newfile:
            for chunk in uploadf.chunks():
                newfile.write(chunk)
        newfile.close()

        #open the file to extract data
        csv_file = open('newitemslist.csv')
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for line in csv_reader:
            if len(line)<=3:
                    newItem =addnewitem(line[0],line[1],line[2])
                    if newItem:
                        print('item added')
                    else:
                        print('cant add item')

        csv_file.close()
