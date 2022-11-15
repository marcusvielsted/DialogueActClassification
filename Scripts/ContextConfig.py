#                                       1: no context included

#                                       2: only context label pre original text
#                                       3: only context sender pre original text
#                                       4: only context text pre original text

#                                       5: only context label post original text
#                                       6: only context sender post original text
#                                       7: only context text post original text

#                                       8: context label + sender pre original text
#                                       9: context label + text pre original text
#                                       10: context label + sender + text pre original text
#                                       11: context label + text + sender pre original text
#                                       12: context sender + label pre original text
#                                       13: context sender + Text pre original text
#                                       14: context sender  + Label + Text pre original text
#                                       15: context sender + Text + Label pre original text
#                                       16: context text + sender pre original text
#                                       17: context text + label pre original text
#                                       18: context text + sender + label pre original text
#                                       19: context text + label + sender pre original text

#                                       20: context label + sender post original text
#                                       21: context label + text post original text
#                                       22: context label + sender + text post original text
#                                       23: context label + text + sender post original text
#                                       24: context sender + label post original text
#                                       25: context sender + Text post original text
#                                       26: context sender  + Label + Text post original text
#                                       27: context sender + Text + Label post original text
#                                       28: context text + sender post original text
#                                       29: context text + label post original text
#                                       30: context text + sender + label post original text
#                                       31: context text + label + sender post original text



class ContextConfigInDomain:
    def __init__(self,context_Config,TargetLabel, d1_Train_Meta, d1_Dev_Meta, d1_Test_Meta):
        self.convert_context_Config = context_Config
        self.targetLabel = TargetLabel
        self.train_NPS_Meta = d1_Train_Meta
        self.dev_NPS_Meta = d1_Dev_Meta
        self.test_NPS_Meta = d1_Test_Meta


    def generateConfig (self):

        #Generate Original text only________________________
        train_text_only = []
        dev_text_only = []
        test_text_only = []
        for text in self.train_NPS_Meta:
            train_text_only.append(text[3])
        for text in self.dev_NPS_Meta:
            dev_text_only.append(text[3])
        for text in self.test_NPS_Meta:
            test_text_only.append(text[3])

        #Generate Context label only________________________
        train_context_label_only = []
        dev_context_label_only = []
        test_context_label_only = []
        if self.targetLabel == "Gold":
            for text in self.train_NPS_Meta:
                train_context_label_only.append(text[4])
            for text in self.dev_NPS_Meta:
                dev_context_label_only.append(text[4])
            for text in self.test_NPS_Meta:
                test_context_label_only.append(text[4])
        elif self.targetLabel =="Predicted":
            for text in self.train_NPS_Meta:
                train_context_label_only.append(text[8])
            for text in self.dev_NPS_Meta:
                dev_context_label_only.append(text[8])
            for text in self.test_NPS_Meta:
                test_context_label_only.append(text[8])


        #Generate Context sender only________________________
        train_context_Sender_only = []
        dev_context_Sender_only = []
        test_context_Sender_only = []
        for text in self.train_NPS_Meta:
            train_context_Sender_only.append(text[5])
        for text in self.dev_NPS_Meta:
            dev_context_Sender_only.append(text[5])
        for text in self.test_NPS_Meta:
            test_context_Sender_only.append(text[5])
            

        #Generate Context text only________________________
        train_context_Text_only = []
        dev_context_Text_only = []
        test_context_Text_only = []
        for text in self.train_NPS_Meta:
            train_context_Text_only.append(text[6])
        for text in self.dev_NPS_Meta:
            dev_context_Text_only.append(text[6])
        for text in self.test_NPS_Meta:
            test_context_Text_only.append(text[6])
        
        
        self.train_context_Pre = "" 
        self.train_context_Post= ""
        self.dev_context_Pre = ""
        self.dev_context_Post= ""
        self.test_context_Pre= ""
        self.test_context_Post = ""


        # No context wanted. Only returns pure input text
        if self.convert_context_Config == 1:
            return train_text_only, dev_text_only, test_text_only 
        
        
        #Context wanted. Setting up the different configurations  
        elif self.convert_context_Config > 1:      
            #                                       2: only context label pre original text
            if self.convert_context_Config == 2:
                self.train_context_Pre = train_context_label_only
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_context_label_only
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_context_label_only
                self.test_context_Post = test_text_only


            #                                       3: only context sender pre original text

            elif self.convert_context_Config == 3:
                self.train_context_Pre = train_context_Sender_only
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_context_Sender_only
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_context_Sender_only
                self.test_context_Post = test_text_only

            #                                       4: only context text pre original text

            elif self.convert_context_Config == 4:
                self.train_context_Pre = train_context_Text_only
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_context_Text_only
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_context_Text_only
                self.test_context_Post = test_text_only
            
            #                                       5: only context label post original text
                
            elif self.convert_context_Config == 5:
                self.train_context_Pre = train_text_only
                self.train_context_Post = train_context_label_only
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_context_label_only
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_context_label_only


            #                                       6: only context sender post original text

            elif self.convert_context_Config == 6:
                self.train_context_Pre = train_text_only
                self.train_context_Post = train_context_Sender_only
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_context_Sender_only
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_context_Sender_only
                
                
            #                                       7: only context text post original text
                
            elif self.convert_context_Config == 7:
                self.train_context_Pre = train_text_only
                self.train_context_Post = train_context_Text_only
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_context_Text_only
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_context_Text_only


            #                                       8: context label + sender pre original text

            elif self.convert_context_Config == 8:
                train_config8 = []
                dev_config8 = []
                test_config8 = []

                for i in range(len(train_context_label_only)):
                    train_config8.append(train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config8.append(dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config8.append(test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_config8
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_config8
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_config8
                self.test_context_Post = test_text_only


            #                                       9: context label + text pre original text

            elif self.convert_context_Config == 9:
                train_config9 = []
                dev_config9 = []
                test_config9 = []

                for i in range(len(train_context_label_only)):
                    train_config9.append(train_context_label_only[i] +" [SEP] " + train_context_Text_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config9.append(dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config9.append(test_context_label_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_config9
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_config9
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_config9
                self.test_context_Post = test_text_only
                
                

            #                                       10: context label + sender + text pre original text
                
            elif self.convert_context_Config == 10:
                train_config10 = []
                dev_config10 = []
                test_config10 = []

                for i in range(len(train_context_label_only)):
                    train_config10.append(train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i] +" [SEP] " + train_context_Text_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config10.append(dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i] +" [SEP] " + dev_context_Text_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config10.append(test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_config10
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_config10
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_config10
                self.test_context_Post = test_text_only


            #                                       11: context label + text + sender pre original text
            
            elif self.convert_context_Config == 11:
                train_config11 = []
                dev_config11 = []
                test_config11 = []

                for i in range(len(train_context_label_only)):
                    train_config11.append(train_context_label_only[i] +" [SEP] " + train_context_Text_only[i] +" [SEP] " + train_context_Sender_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config11.append(dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i] +" [SEP] " + dev_context_Sender_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config11.append(test_context_label_only[i] +" [SEP] " + test_context_Text_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_config11
                self.train_context_Post = train_text_only

                self.dev_context_Pre = dev_config11
                self.dev_context_Post = dev_text_only

                self.test_context_Pre = test_config11
                self.test_context_Post = test_text_only    
                
                

            #                                       12: context sender + label pre original text

            elif self.convert_context_Config == 12:
                train_config12 = []
                dev_config12 = []
                test_config12 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config12.append(train_context_Sender_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config12.append(dev_context_Sender_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config12.append(test_context_Sender_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_config12
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config12
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config12
                self.test_context_Post = test_text_only
                
                
                
                
            #                                       13: context sender + Text pre original text

            elif self.convert_context_Config == 13:
                train_config13 = []
                dev_config13 = []
                test_config13 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config13.append(train_context_Sender_only[i]  +" [SEP] " + train_context_Text_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config13.append(dev_context_Sender_only[i]  +" [SEP] " + dev_context_Text_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config13.append(test_context_Sender_only[i]  +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_config13
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config13
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config13
                self.test_context_Post = test_text_only


            #                                       14: context sender  + Label + Text pre original text

            elif self.convert_context_Config == 14:
                train_config14 = []
                dev_config14 = []
                test_config14 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config14.append(train_context_Sender_only[i] +" [SEP] " + train_context_label_only[i] +" [SEP] " + train_context_Text_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config14.append(dev_context_Sender_only[i] +" [SEP] " + dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config14.append(test_context_Sender_only[i] +" [SEP] " + test_context_label_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_config14
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config14
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config14
                self.test_context_Post = test_text_only
                
            
            
            #                                       15: context sender + Text + Label pre original text
            
            elif self.convert_context_Config == 15:
                train_config15 = []
                dev_config15 = []
                test_config15 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config15.append(train_context_Sender_only[i] +" [SEP] " + train_context_Text_only[i] +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config15.append(dev_context_Sender_only[i] +" [SEP] " + dev_context_Text_only[i] +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config15.append(test_context_Sender_only[i] +" [SEP] " + test_context_Text_only[i] +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_config15
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config15
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config15
                self.test_context_Post = test_text_only



            #                                       16: context text + sender pre original text


            elif self.convert_context_Config == 16:
                train_config16 = []
                dev_config16 = []
                test_config16 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config16.append(train_context_Text_only[i]  +" [SEP] " + train_context_Sender_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config16.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_Sender_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config16.append(test_context_Text_only[i]  +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_config16
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config16
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config16
                self.test_context_Post = test_text_only


            #                                       17: context text + label pre original text

            elif self.convert_context_Config == 17:
                train_config17 = []
                dev_config17 = []
                test_config17 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config17.append(train_context_Text_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config17.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config17.append(test_context_Text_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_config17
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config17
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config17
                self.test_context_Post = test_text_only
                


            #                                       18: context text + sender + label pre original text
                
            elif self.convert_context_Config == 18:
                train_config18 = []
                dev_config18 = []
                test_config18 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config18.append(train_context_Text_only[i]  +" [SEP] " + train_context_Sender_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config18.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_Sender_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config18.append(test_context_Text_only[i]  +" [SEP] " + test_context_Sender_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_config18
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config18
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config18
                self.test_context_Post = test_text_only

            #                                       19: context text + label + sender pre original text

            elif self.convert_context_Config == 19:
                train_config19 = []
                dev_config19 = []
                test_config19 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config19.append(train_context_Text_only[i]  +" [SEP] " + train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config19.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config19.append(test_context_Text_only[i]  +" [SEP] " + test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_config19
                self.train_context_Post = train_text_only
                self.dev_context_Pre = dev_config19
                self.dev_context_Post = dev_text_only
                self.test_context_Pre = test_config19
                self.test_context_Post = test_text_only
                

            #                                       20: context label + sender post original text

            elif self.convert_context_Config == 20:
                train_config20 = []
                dev_config20 = []
                test_config20 = []

                for i in range(len(train_context_label_only)):
                    train_config20.append(train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config20.append(dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config20.append(test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config20

                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config20

                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config20


            #                                       21: context label + text post original text

            elif self.convert_context_Config == 21:
                train_config21 = []
                dev_config21 = []
                test_config21 = []

                for i in range(len(train_context_label_only)):
                    train_config21.append(train_context_label_only[i] +" [SEP] " + train_context_Text_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config21.append(dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config21.append(test_context_label_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config21

                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config21

                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config21
                
                

            #                                       22: context label + sender + text post original text

            elif self.convert_context_Config == 22:
                train_config22 = []
                dev_config22 = []
                test_config22 = []

                for i in range(len(train_context_label_only)):
                    train_config22.append(train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i] +" [SEP] " + train_context_Text_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config22.append(dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i] +" [SEP] " + dev_context_Text_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config22.append(test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config22

                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config22

                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config22


            #                                       23: context label + text + sender post original text

            elif self.convert_context_Config == 23:
                train_config23 = []
                dev_config23 = []
                test_config23 = []

                for i in range(len(train_context_label_only)):
                    train_config23.append(train_context_label_only[i] +" [SEP] " + train_context_Text_only[i] +" [SEP] " + train_context_Sender_only[i])
                
                for i in range(len(dev_context_label_only)):
                    dev_config23.append(dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i] +" [SEP] " + dev_context_Sender_only[i])
                
                for i in range(len(test_context_label_only)):
                    test_config23.append(test_context_label_only[i] +" [SEP] " + test_context_Text_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config23

                self.dev_context_Pre = dev_text_only
                self.dev_context_Post =dev_config23

                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config23
                
                

            #                                       24: context sender + label post original text

            elif self.convert_context_Config == 24:
                train_config24 = []
                dev_config24 = []
                test_config24 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config24.append(train_context_Sender_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config24.append(dev_context_Sender_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config24.append(test_context_Sender_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config24
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config24
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config24
                
                
                
                
            #                                       25: context sender + Text post original text

            elif self.convert_context_Config == 25:
                train_config25 = []
                dev_config25 = []
                test_config25 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config25.append(train_context_Sender_only[i]  +" [SEP] " + train_context_Text_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config25.append(dev_context_Sender_only[i]  +" [SEP] " + dev_context_Text_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config25.append(test_context_Sender_only[i]  +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config25
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config25
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config25


            #                                       26: context sender  + Label + Text post original text

            elif self.convert_context_Config == 26:
                train_config26 = []
                dev_config26 = []
                test_config26 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config26.append(train_context_Sender_only[i] +" [SEP] " + train_context_label_only[i] +" [SEP] " + train_context_Text_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config26.append(dev_context_Sender_only[i] +" [SEP] " + dev_context_label_only[i] +" [SEP] " + dev_context_Text_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config26.append(test_context_Sender_only[i] +" [SEP] " + test_context_label_only[i] +" [SEP] " + test_context_Text_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config26
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config26
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config26
                
            #                                       27: context sender + Text + Label post original text
            
            elif self.convert_context_Config == 27:
                train_config27 = []
                dev_config27 = []
                test_config27 = []
                    
                for i in range(len(train_context_Sender_only)):
                    train_config27.append(train_context_Sender_only[i] +" [SEP] " + train_context_Text_only[i] +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Sender_only)):
                    dev_config27.append(dev_context_Sender_only[i] +" [SEP] " + dev_context_Text_only[i] +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Sender_only)):
                    test_config27.append(test_context_Sender_only[i] +" [SEP] " + test_context_Text_only[i] +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config27
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config27
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config27


            #                                       28: context text + sender post original text


            elif self.convert_context_Config == 28:
                train_config28 = []
                dev_config28 = []
                test_config28 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config28.append(train_context_Text_only[i]  +" [SEP] " + train_context_Sender_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config28.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_Sender_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config28.append(test_context_Text_only[i]  +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config28
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config28
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config28


            #                                       29: context text + label post original text

            elif self.convert_context_Config == 29:
                train_config29 = []
                dev_config29 = []
                test_config29 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config29.append(train_context_Text_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config29.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config29.append(test_context_Text_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config29
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config29
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config29
                

            #                                       30: context text + sender + label post original text
                
            elif self.convert_context_Config == 30:
                train_config30 = []
                dev_config30 = []
                test_config30 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config30.append(train_context_Text_only[i]  +" [SEP] " + train_context_Sender_only[i]  +" [SEP] " + train_context_label_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config30.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_Sender_only[i]  +" [SEP] " + dev_context_label_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config30.append(test_context_Text_only[i]  +" [SEP] " + test_context_Sender_only[i]  +" [SEP] " + test_context_label_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config30
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config30
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config30


            #                                       31: context text + label + sender post original text

            elif self.convert_context_Config == 31:
                train_config31 = []
                dev_config31 = []
                test_config31 = []
                    
                for i in range(len(train_context_Text_only)):
                    train_config31.append(train_context_Text_only[i]  +" [SEP] " + train_context_label_only[i] +" [SEP] " + train_context_Sender_only[i])

                for i in range(len(dev_context_Text_only)):
                    dev_config31.append(dev_context_Text_only[i]  +" [SEP] " + dev_context_label_only[i] +" [SEP] " + dev_context_Sender_only[i])

                for i in range(len(test_context_Text_only)):
                    test_config31.append(test_context_Text_only[i]  +" [SEP] " + test_context_label_only[i] +" [SEP] " + test_context_Sender_only[i])

                self.train_context_Pre = train_text_only
                self.train_context_Post = train_config31
                self.dev_context_Pre = dev_text_only
                self.dev_context_Post = dev_config31
                self.test_context_Pre = test_text_only
                self.test_context_Post = test_config31
                
            
        return self.train_context_Pre, self.train_context_Post, self.dev_context_Pre,self.dev_context_Post, self.test_context_Pre, self.test_context_Post 
    


















class ContextConfigCrossDomain:
    def __init__(self,context_Config,TargetLabel, d1_Train_Meta, d1_Dev_Meta, d2_tune_meta, d2_test_Meta):
        self.convert_context_Config = context_Config
        self.targetLabel = TargetLabel
        self.train_NPS_Meta = d1_Train_Meta
        self.dev_NPS_Meta = d1_Dev_Meta
        self.tune_Reddit_Meta = d2_tune_meta
        self.test_Reddit_Meta = d2_test_Meta
    
    
    def generateConfig (self):
        #Generate Original text only________________________
        NPS_train_text = []
        NPS_dev_text = []
        Reddit_tune_text = []
        Reddit_test_text = []

        for text in self.train_NPS_Meta:
            NPS_train_text.append(text[3])
        for text in self.dev_NPS_Meta:
            NPS_dev_text.append(text[3])
        for text in self.tune_Reddit_Meta:
            Reddit_tune_text.append(text[3])
        for text in self.test_Reddit_Meta:
            Reddit_test_text.append(text[3])

        #Generate Context label only________________________
        NPS_train_context_label_only = []
        NPS_dev_context_label_only = []
        Reddit_tune_context_label_only = []
        Reddit_test_context_label_only = []
        if self.targetLabel == "Gold":
            for text in self.train_NPS_Meta:
                NPS_train_context_label_only.append(text[4])
            for text in self.dev_NPS_Meta:
                NPS_dev_context_label_only.append(text[4])
            for text in self.tune_Reddit_Meta:
                Reddit_tune_context_label_only.append(text[4])
            for text in self.test_Reddit_Meta:
                Reddit_test_context_label_only.append(text[4])
        elif self.targetLabel == "Predicted":
            for text in self.train_NPS_Meta:
                NPS_train_context_label_only.append(text[8])
            for text in self.dev_NPS_Meta:
                NPS_dev_context_label_only.append(text[8])
            for text in self.tune_Reddit_Meta:
                Reddit_tune_context_label_only.append(text[8])
            for text in self.test_Reddit_Meta:
                Reddit_test_context_label_only.append(text[8])

        #Generate Context sender only________________________
        NPS_train_context_Sender_only = []
        NPS_dev_context_Sender_only = []
        Reddit_tune_context_Sender_only = []
        Reddit_test_context_Sender_only = []
        for text in self.train_NPS_Meta:
            NPS_train_context_Sender_only.append(text[5])
        for text in self.dev_NPS_Meta:
            NPS_dev_context_Sender_only.append(text[5])
        for text in self.tune_Reddit_Meta:
            Reddit_tune_context_Sender_only.append(text[5])
        for text in self.test_Reddit_Meta:
            Reddit_test_context_Sender_only.append(text[5])

        
              #Generate Context text only________________________
        NPS_train_context_Text_only = []
        NPS_dev_context_Text_only = []
        Reddit_tune_context_Text_only = []
        Reddit_test_context_Text_only = []
        for text in self.train_NPS_Meta:
            NPS_train_context_Text_only.append(text[6])
        for text in self.dev_NPS_Meta:
            NPS_dev_context_Text_only.append(text[6])
        for text in self.tune_Reddit_Meta:
            Reddit_tune_context_Text_only.append(text[6])
        for text in self.test_Reddit_Meta:
            Reddit_test_context_Text_only.append(text[6])



        # __________________________________________________COINTEXT INCLUSION HERE_____________________________________________
        self.NPS_train_context_Pre = "" 
        self.NPS_train_context_Post = ""
        self.NPS_dev_context_Pre = ""
        self.NPS_dev_context_Post = ""
        self.Reddit_tune_context_Pre = ""
        self.Reddit_tune_context_Post = ""
        self.Reddit_test_context_Pre = ""
        self.Reddit_test_context_Post = ""
        
             # No context wanted. Only returns pure input text
        if self.convert_context_Config == 1:
            return NPS_train_text, NPS_dev_text, Reddit_tune_text, Reddit_test_text
        
        
        #Context wanted. Setting up the different configurations  
        elif self.convert_context_Config > 1:      
            #                                       2: only context label pre original text
            if self.convert_context_Config == 2:
                self.NPS_train_context_Pre = NPS_train_context_label_only
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_context_label_only
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_context_label_only
                self.Reddit_tune_context_Post = Reddit_tune_text

                self.Reddit_test_context_Pre = Reddit_test_context_label_only
                self.Reddit_test_context_Post = Reddit_test_text


            #                                       3: only context sender pre original text

            elif self.convert_context_Config == 3:
                self.NPS_train_context_Pre = NPS_train_context_Sender_only
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_context_Sender_only
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_context_Sender_only
                self.Reddit_tune_context_Post = Reddit_tune_text

                self.Reddit_test_context_Pre = Reddit_test_context_Sender_only
                self.Reddit_test_context_Post = Reddit_test_text

            #                                       4: only context text pre original text

            elif self.convert_context_Config == 4:
                self.NPS_train_context_Pre = NPS_train_context_Text_only
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_context_Text_only
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_context_Text_only
                self.Reddit_tune_context_Post = Reddit_tune_text

                self.Reddit_test_context_Pre = Reddit_test_context_Text_only
                self.Reddit_test_context_Post = Reddit_test_text

            
            #                                       5: only context label post original text
                
            elif self.convert_context_Config == 5:
                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_context_label_only

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_context_label_only

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_context_label_only

                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_context_label_only



            #                                       6: only context sender post original text

            elif self.convert_context_Config == 6:
                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_context_Sender_only

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_context_Sender_only

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_context_Sender_only

                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_context_Sender_only
                
            #                                       7: only context text post original text
                
            elif self.convert_context_Config == 7:
                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_context_Text_only

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_context_Text_only

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_context_Text_only

                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_context_Text_only


            #                                       8: context label + sender pre original text

            elif self.convert_context_Config == 8:
                NPS_train_config8 = []
                NPS_dev_config8 = []
                Reddit_tune_config8 = []
                Reddit_test_config8 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config8.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config8.append(NPS_dev_context_label_only[i] +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config8.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config8.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_config8
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config8
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config8
                self.Reddit_tune_context_Post = Reddit_tune_text

                self.Reddit_test_context_Pre = Reddit_test_config8
                self.Reddit_test_context_Post = Reddit_test_text



            #                                       9: context label + text pre original text

            elif self.convert_context_Config == 9:
                NPS_train_config9 = []
                NPS_dev_config9 = []
                Reddit_tune_config9 = []
                Reddit_test_config9 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config9.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config9.append(NPS_dev_context_label_only[i] +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config9.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config9.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_config9
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config9
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config9
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config9
                self.Reddit_test_context_Post = Reddit_test_text
                
                

            #                                       10: context label + sender + text pre original text
                
            elif self.convert_context_Config == 10:
                NPS_train_config10 = []
                NPS_dev_config10 = []
                Reddit_tune_config10 = []
                Reddit_test_config10 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config10.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config10.append(NPS_dev_context_label_only[i]+" [SEP] " + NPS_dev_context_Sender_only[i]  +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config10.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config10.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i]+" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_config10
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config10
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config10
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config10
                self.Reddit_test_context_Post = Reddit_test_text


            #                                       11: context label + text + sender pre original text
            
            elif self.convert_context_Config == 11:
                NPS_train_config11 = []
                NPS_dev_config11 = []
                Reddit_tune_config11 = []
                Reddit_test_config11 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config11.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config11.append(NPS_dev_context_label_only[i]+" [SEP] " + NPS_dev_context_Text_only[i]  +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config11.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config11.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Text_only[i]+" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_config11
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config11
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config11
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config11
                self.Reddit_test_context_Post = Reddit_test_text
                

            #                                       12: context sender + label pre original text

            elif self.convert_context_Config == 12:
                NPS_train_config12 = []
                NPS_dev_config12 = []
                Reddit_tune_config12 = []
                Reddit_test_config12 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config12.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config12.append(NPS_dev_context_Sender_only[i] +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config12.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config12.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_config12
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config12
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config12
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config12
                self.Reddit_test_context_Post = Reddit_test_text
                
                
                
                
            #                                       13: context sender + Text pre original text

            elif self.convert_context_Config == 13:
                NPS_train_config13 = []
                NPS_dev_config13 = []
                Reddit_tune_config13 = []
                Reddit_test_config13 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config13.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config13.append(NPS_dev_context_Sender_only[i] +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config13.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config13.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_config13
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config13
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config13
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config13
                self.Reddit_test_context_Post = Reddit_test_text


            #                                       14: context sender  + Label + Text pre original text

            elif self.convert_context_Config == 14:
                NPS_train_config14 = []
                NPS_dev_config14 = []
                Reddit_tune_config14 = []
                Reddit_test_config14 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config14.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config14.append(NPS_dev_context_Sender_only[i]+" [SEP] " + NPS_dev_context_label_only[i]  +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config14.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config14.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_label_only[i]+" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_config14
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config14
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config14
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config14
                self.Reddit_test_context_Post = Reddit_test_text
                
            
            
            #                                       15: context sender + Text + Label pre original text
            
            elif self.convert_context_Config == 15:
                NPS_train_config15 = []
                NPS_dev_config15 = []
                Reddit_tune_config15 = []
                Reddit_test_config15 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config15.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config15.append(NPS_dev_context_Sender_only[i]+" [SEP] " + NPS_dev_context_Text_only[i]  +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config15.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config15.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_Text_only[i]+" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_config15
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config15
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config15
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config15
                self.Reddit_test_context_Post = Reddit_test_text
                


            #                                       16: context text + sender pre original text


            elif self.convert_context_Config == 16:
                NPS_train_config16 = []
                NPS_dev_config16 = []
                Reddit_tune_config16 = []
                Reddit_test_config16 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config16.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config16.append(NPS_dev_context_Text_only[i] +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config16.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config16.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_config16
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config16
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config16
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config16
                self.Reddit_test_context_Post = Reddit_test_text


            #                                       17: context text + label pre original text

            elif self.convert_context_Config == 17:
                NPS_train_config17 = []
                NPS_dev_config17 = []
                Reddit_tune_config17 = []
                Reddit_test_config17 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config17.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config17.append(NPS_dev_context_Text_only[i] +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config17.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config17.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_config17
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config17
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config17
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config17
                self.Reddit_test_context_Post = Reddit_test_text



            #                                       18: context text + sender + label pre original text
                
            elif self.convert_context_Config == 18:
                NPS_train_config18 = []
                NPS_dev_config18 = []
                Reddit_tune_config18 = []
                Reddit_test_config18 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config18.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config18.append(NPS_dev_context_Text_only[i]+" [SEP] " + NPS_dev_context_Sender_only[i]  +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config18.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config18.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i]+" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_config18
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config18
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config18
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config18
                self.Reddit_test_context_Post = Reddit_test_text
                

            #                                       19: context text + label + sender pre original text

            elif self.convert_context_Config == 19:
                NPS_train_config19 = []
                NPS_dev_config19 = []
                Reddit_tune_config19 = []
                Reddit_test_config19 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config19.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config19.append(NPS_dev_context_Text_only[i]+" [SEP] " + NPS_dev_context_label_only[i]  +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config19.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config19.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_label_only[i]+" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_config19
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config19
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config19
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config19
                self.Reddit_test_context_Post = Reddit_test_text
                

            #                                       20: context label + sender post original text

            elif self.convert_context_Config == 20:
                NPS_train_config20 = []
                NPS_dev_config20 = []
                Reddit_tune_config20 = []
                Reddit_test_config20 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config20.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config20.append(NPS_dev_context_label_only[i] +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config20.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config20.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config20

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config20

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config20

                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config20



            #                                       21: context label + text post original text

            elif self.convert_context_Config == 21:
                NPS_train_config21 = []
                NPS_dev_config21 = []
                Reddit_tune_config21 = []
                Reddit_test_config21 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config21.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config21.append(NPS_dev_context_label_only[i] +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config21.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config21.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config21

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config21

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config21
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config21
                
                

            #                                       22: context label + sender + text post original text
                
            elif self.convert_context_Config == 22:
                NPS_train_config22 = []
                NPS_dev_config22 = []
                Reddit_tune_config22 = []
                Reddit_test_config22 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config22.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config22.append(NPS_dev_context_label_only[i]+" [SEP] " + NPS_dev_context_Sender_only[i]  +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config22.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config22.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i]+" [SEP] " + Reddit_test_context_Text_only[i])


                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config22

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config22

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config22
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config22


            #                                       23: context label + text + sender post original text
            
            elif self.convert_context_Config == 23:
                NPS_train_config23 = []
                NPS_dev_config23 = []
                Reddit_tune_config23 = []
                Reddit_test_config23 = []

                for i in range(len(NPS_train_context_label_only)):
                    NPS_train_config23.append(NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_label_only)):
                    NPS_dev_config23.append(NPS_dev_context_label_only[i]+" [SEP] " + NPS_dev_context_Text_only[i]  +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_label_only)):
                    Reddit_tune_config23.append(Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_label_only)):
                    Reddit_test_config23.append(Reddit_test_context_label_only[i] +" [SEP] " + Reddit_test_context_Text_only[i]+" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config23

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config23

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config23
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config23
                

            #                                       24: context sender + label post original text

            elif self.convert_context_Config == 24:
                NPS_train_config24 = []
                NPS_dev_config24 = []
                Reddit_tune_config24 = []
                Reddit_test_config24 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config24.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config24.append(NPS_dev_context_Sender_only[i] +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config24.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config24.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_config24
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config24
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config24
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config24
                self.Reddit_test_context_Post = Reddit_test_text
                
                
                
                
            #                                       25: context sender + Text post original text

            elif self.convert_context_Config == 25:
                NPS_train_config25 = []
                NPS_dev_config25 = []
                Reddit_tune_config25 = []
                Reddit_test_config25 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config25.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config25.append(NPS_dev_context_Sender_only[i] +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config25.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config25.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config25

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config25

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config25
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config25


            #                                       26: context sender  + Label + Text post original text

            elif self.convert_context_Config == 26:
                NPS_train_config26 = []
                NPS_dev_config26 = []
                Reddit_tune_config26 = []
                Reddit_test_config26 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config26.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Text_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config26.append(NPS_dev_context_Sender_only[i]+" [SEP] " + NPS_dev_context_label_only[i]  +" [SEP] " + NPS_dev_context_Text_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config26.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config26.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_label_only[i]+" [SEP] " + Reddit_test_context_Text_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config26

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config26

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config26
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config26
                
            
            
            #                                       27: context sender + Text + Label post original text
            
            elif self.convert_context_Config == 27:
                NPS_train_config27 = []
                NPS_dev_config27 = []
                Reddit_tune_config27 = []
                Reddit_test_config27 = []

                for i in range(len(NPS_train_context_Sender_only)):
                    NPS_train_config27.append(NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Sender_only)):
                    NPS_dev_config27.append(NPS_dev_context_Sender_only[i]+" [SEP] " + NPS_dev_context_Text_only[i]  +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Sender_only)):
                    Reddit_tune_config27.append(Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Sender_only)):
                    Reddit_test_config27.append(Reddit_test_context_Sender_only[i] +" [SEP] " + Reddit_test_context_Text_only[i]+" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config27

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config27

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config27
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config27
                


            #                                       28: context text + sender post original text


            elif self.convert_context_Config == 28:
                NPS_train_config28 = []
                NPS_dev_config28 = []
                Reddit_tune_config28 = []
                Reddit_test_config28 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config28.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config28.append(NPS_dev_context_Text_only[i] +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config28.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config28.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config28

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config28

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config28
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config28


            #                                       29: context text + label post original text

            elif self.convert_context_Config == 29:
                NPS_train_config29 = []
                NPS_dev_config29 = []
                Reddit_tune_config29 = []
                Reddit_test_config29 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config29.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config29.append(NPS_dev_context_Text_only[i] +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config29.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config29.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config29

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config29

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config29
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config29



            #                                       30: context text + sender + label post original text
                
            elif self.convert_context_Config == 30:
                NPS_train_config30 = []
                NPS_dev_config30 = []
                Reddit_tune_config30 = []
                Reddit_test_config30 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config30.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_Sender_only[i] +" [SEP] " + NPS_train_context_label_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config30.append(NPS_dev_context_Text_only[i]+" [SEP] " + NPS_dev_context_Sender_only[i]  +" [SEP] " + NPS_dev_context_label_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config30.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i] +" [SEP] " + Reddit_tune_context_label_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config30.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_Sender_only[i]+" [SEP] " + Reddit_test_context_label_only[i])



                self.NPS_train_context_Pre = NPS_train_text
                self.NPS_train_context_Post = NPS_train_config30

                self.NPS_dev_context_Pre = NPS_dev_text
                self.NPS_dev_context_Post = NPS_dev_config30

                self.Reddit_tune_context_Pre = Reddit_tune_text
                self.Reddit_tune_context_Post = Reddit_tune_config30
                
                self.Reddit_test_context_Pre = Reddit_test_text
                self.Reddit_test_context_Post = Reddit_test_config30
                

            #                                       31: context text + label + sender post original text

            elif self.convert_context_Config == 31:
                NPS_train_config31 = []
                NPS_dev_config31 = []
                Reddit_tune_config31 = []
                Reddit_test_config31 = []

                for i in range(len(NPS_train_context_Text_only)):
                    NPS_train_config31.append(NPS_train_context_Text_only[i] +" [SEP] " + NPS_train_context_label_only[i] +" [SEP] " + NPS_train_context_Sender_only[i])
                
                for i in range(len(NPS_dev_context_Text_only)):
                    NPS_dev_config31.append(NPS_dev_context_Text_only[i]+" [SEP] " + NPS_dev_context_label_only[i]  +" [SEP] " + NPS_dev_context_Sender_only[i])
                
                for i in range(len(Reddit_tune_context_Text_only)):
                    Reddit_tune_config31.append(Reddit_tune_context_Text_only[i] +" [SEP] " + Reddit_tune_context_label_only[i] +" [SEP] " + Reddit_tune_context_Sender_only[i])

                for i in range(len(Reddit_test_context_Text_only)):
                    Reddit_test_config31.append(Reddit_test_context_Text_only[i] +" [SEP] " + Reddit_test_context_label_only[i]+" [SEP] " + Reddit_test_context_Sender_only[i])



                self.NPS_train_context_Pre = NPS_train_config31
                self.NPS_train_context_Post = NPS_train_text

                self.NPS_dev_context_Pre = NPS_dev_config31
                self.NPS_dev_context_Post = NPS_dev_text

                self.Reddit_tune_context_Pre = Reddit_tune_config31
                self.Reddit_tune_context_Post = Reddit_tune_text
                
                self.Reddit_test_context_Pre = Reddit_test_config31
                self.Reddit_test_context_Post = Reddit_test_text
                

                
            
        return self.NPS_train_context_Pre, self.NPS_train_context_Post, self.NPS_dev_context_Pre, self.NPS_dev_context_Post, self.Reddit_tune_context_Pre, self.Reddit_tune_context_Post, self.Reddit_test_context_Pre, self.Reddit_test_context_Post