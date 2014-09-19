#import the csv module
import csv
from pip._vendor.html5lib.html5parser import method_decorator_metaclass
from IPython.testing.tools import pair_fail_msg

class PortfolioConcentration(object):
    
    #open a comma delimited file and return the output
    #I wrote this function so that it takes any column and returns the sum of market value by that column    
    def GetMeasureTotalBySlice(self, slice, measure):
        try:
            positionsFile = None
            # raw string
            fileName = r".\PortfolioAppraisalReport.csv"
            if not csv.Sniffer().has_header(fileName):
                raise Exception("headers expected in position file. FileName: " + fileName)
            positionsFile = open(fileName, 'rt')
            dictReader = csv.DictReader(positionsFile)
            #dictReader is list of dictionaries where the keys are the column headers and the values represent one row of values
            
            dictTag = {}
            #iterate over 
            for dictRow in dictReader:
                mv = dictRow[measure]
                strat = dictRow[slice]
                #need to cast to float
                if(dictTag.has_key(strat)):
                    dictTag[strat] += float(mv)
                else:
                    dictTag[strat] = float(mv)
            return dictTag
        except Exception, e:
            print e
            raise e
        finally:
            #print 'Finalizer called'
            if positionsFile != None :
                positionsFile.close()
    
    
    #This function should accept the dictionary and return that max and the min value in the dictionary
    def GetTopandBottomSlices(self, sliceData):
        
        #what do you think this method should return
        #get the min and max value in dictionary
        values = sliceData.values();
        minValue = min(values);
        maxValue = max(values);
        #make dict of min and max pair in dict parameter
        #have potential to include multiple pairs that all have min or max value
        dictTopBottom = {"min" : {}, "max" : {}};
        dictTopBottom["min"] = {key : sliceData[key] for key in sliceData.keys() if sliceData[key] == minValue}
        dictTopBottom["max"] = {key : sliceData[key] for key in sliceData.keys() if sliceData[key] == maxValue}
        
        '''
        dictTBSlice = {"min" : [], "max" : []};
        dictTBSlice["min"] = [key for key in sliceData.keys() if sliceData[key] == minv]
        dictTBSlice["max"] = [key for key in sliceData.keys() if sliceData[key] == maxv]
        '''
        '''
        for k in sliceData:
            if(sliceData[k] == minv):
                dictTBSlice["min"].append(k);
            elif(sliceData[k] == maxv):
                dictTBSlice["max"].append(k);                        
        '''
        return dictTopBottom
        #return dictTBSlice;

#This class represent the Assignment 1
#every method in it represents a question
class HW1(object):      
    
    def QuestionSample(self): 
        #how do you want to query this portfolio
        slice = "StrategyDesc"
        measure = "BaseMarketValue"
        portfolioConcentration = PortfolioConcentration()
        tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
        print "Sample"
        print tagData
        print portfolioConcentration.GetTopandBottomSlices(tagData);
        print
        
    def Question5(self): 
        #how do you want to query this portfolio
        slice = "StrategyDesc"
        measure = "BaseMarketValue"
        portfolioConcentration = PortfolioConcentration()
        tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
        print "Q5"
        print "Firm's exposure to Value Equities is", tagData["Value Equities"]
        print
        
    def Question7(self): 
        #how do you want to query this portfolio
        slice = "SecurityDesc"
        measure = "BaseMarketValue"
        portfolioConcentration = PortfolioConcentration()
        tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
        tbDict = portfolioConcentration.GetTopandBottomSlices(tagData);
        print "Q7"
        print "Firms biggest short position:"
        #print every security that has the min position 
        for key in tbDict["min"]:
            print key,
        print "with position of " + str(tbDict["min"][tbDict["min"].keys()[0]]) 
        print
    
    def Question8(self): 
        #how do you want to query this portfolio
        slice = "StrategyDesc"
        measure = "YTDTotalPnL"
        portfolioConcentration = PortfolioConcentration()
        tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
        tbDict = portfolioConcentration.GetTopandBottomSlices(tagData);
        print "Q8"
        print "Strategy type top performer of this year: "
        #print every strategy that has the top performs 
        for key in tbDict["max"]:
            print key,
        print "with year-to-date total PnL of " + str(tbDict["max"][tbDict["max"].keys()[0]]) 
        print "Strategy type bottom performer of this year: "
        #print every strategy that has the bottom position 
        for key in tbDict["min"]:
            print key,
        print "with year-to-date total PnL of " + str(tbDict["min"][tbDict["min"].keys()[0]])
        print
        
    def Question9(self): 
        #how do you want to query this portfolio
        slice = "SecurityTypeDesc"
        measure = "YTDTotalPnL"
        portfolioConcentration = PortfolioConcentration()
        tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
        tbDict = portfolioConcentration.GetTopandBottomSlices(tagData);
        print "Q9"
        print "Asset type top performer of this year: "
        #print every asset type that has the top performs
        for key in tbDict["max"]:
            print key,
        print "with year-to-date total PnL of " + str(tbDict["max"][tbDict["max"].keys()[0]]) 
        print "Strategy type bottom performer of this year: "
        #print every asset type that has the bottom performs
        for key in tbDict["min"]:
            print key,
        print "with year-to-date total PnL of " + str(tbDict["min"][tbDict["min"].keys()[0]])
        print  
        
try:
    hw1 = HW1()
    #hw1.QuestionSample();
    hw1.Question5();
    hw1.Question7();
    hw1.Question8();
    hw1.Question9();
    '''
    #how do you want to query this portfolio
    slice = "StrategyDesc"
    measure = "BaseMarketValue"
    portfolioConcentration = PortfolioConcentration()
    tagData = portfolioConcentration.GetMeasureTotalBySlice(slice, measure)
    print tagData
    print portfolioConcentration.GetTopandBottomSlices(tagData);
    '''
    
except Exception, e:
    print e    
        