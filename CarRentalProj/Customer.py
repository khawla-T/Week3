Cars = {
    'Car1':{
        'number':1,
        'price': 50,
        'model':'ui384',
        'rented_flag':0,
    },
    'Car2':{
        'number':2,
        'price': 60,
        'model':'fwe344',
        'rented_flag':0,
    },
    'Car3':{
        'number':3,
        'price': 70,
        'model':'fiu875',
        'rented_flag':0,
    },
    'Car4':{
        'number':4,
        'price': 100,
        'model':'doi287',
        'rented_flag':0,
    }
}

Customer_id_starter = 123 #used to creat IDs

#all cars owned by the store
Store_cars=4    

#all cars rented 
total_car_rented=0

class Customer:
    def __init__(self,name):
        self.name=name
        self.id= Customer_id_starter+1
        self.rented_cars_cus=0    #how many cars are rented by one customer
        self.bill=0
        
        
    def rent_car(self,car_number):
        #if total_car_rented <= Store_cars:    
            ls=[]
            for i in Cars: 
                ls=Cars[i]
                if ls['number'] == car_number:
                    if ls['rented_flag']==0:
                        ls['rented_flag']=1
                        self.rented_cars_cus+=1
                        global total_car_rented
                        total_car_rented+=1
                        print('total car rented',total_car_rented)
                        break
                    else:
                        print("This car alredy rented")
                        break
    

    def return_cars(self,cars_num,bill):
        ls=[]
        for i in Cars: 
            ls=Cars[i]
            if ls['number'] == cars_num:
                if ls['rented_flag']==1:
                    ls['rented_flag']=0
                    self.rented_cars_cus -=1
                    global total_car_rented
                    total_car_rented-=1  
                    self.bill = bill
                    break
                else:
                    print("No such car to return!")
                    break
    
    def list_cars_rented(self):
        ls=[]
        for i in Cars: 
            ls=Cars[i]
            if ls['rented_flag']== 1:
                print(Cars[i],'\n')    
    
    def list_cars_for_rent(self):
        ls=[]
        for i in Cars: 
            ls=Cars[i]
            if ls['rented_flag']== 0:
                print(Cars[i],'\n')
                   