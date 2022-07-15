import logging
logging.basicConfig(filename ="over.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class Ibm:

    def job_info(self,job_dict):
        try:
            logging.info('this function provides job role and annual salary expectations at IBM ')
            for k,v in job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)

    def blog(self):
        print("this function contains blogs for IBM")

ib_obj = Ibm()
logging.info("this is IBM class object %s :" ,ib_obj)
logging.info(ib_obj.job_info({'Data Scientist' : 1200000 ,'SQL Developer':100000}))

class Ineuron(Ibm):

    def job_info(self,job_dict):
        try:
            logging.info('this function provides job role and annual salary expectations at INEURON ')
            for k,v in job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)

in_obj=Ineuron()
logging.info("this is INEURON class object %s :",in_obj)
logging.info("overriding job_info function...")
logging.info(in_obj.job_info({'Data Scientist' : 1200000 ,'SQL Developer':100000 ,'Data Engineer' : 130000 ,'Data Analyst' :900000}))

logging.info("After calling this function we realised that class Inueron object is able to override the function of same name"
             "which was already there is super class with same signature/arguments")








