from inspect import signature
import logging,abc

def handle(name,prev_sig,now_sig,english=True):
    logging.warning("Signature mismatch in %s : %s != %s" if english \
    else "%s参数不同： %s 不等于 %s",
                    name,prev_sig,now_sig)
class MatchSigMeta(abc.ABCMeta):
    def __init__(self,clsname,bases,clsdict):
        #self:new class
        #clsname:new class name
        #bases:base classes
        #clsdict=self.__dict__
        
        #print(clsname)
        #print(clsdict)
        super().__init__(clsname,bases,clsdict)
        new_class_super=super(self,self)#super of the new class
        for name,val in clsdict.items():#get all the items
            if name.startswith('_') or not callable(val):
                continue
                #skips privite & only check metheds
            else:
                #print("Checking")
                prevdef=getattr(new_class_super,name,None)
                #if no such thing,return None
                if prevdef:#if defined before
                    prevsig=signature(prevdef)
                    nowsig=signature(val)
                    #print(prevsig,nowsig)
                    if prevsig != nowsig:#arguments not the same!
                        
                        handle(val.__qualname__,#val's name
                               prevsig,nowsig)
class Root(metaclass=MatchSigMeta):
    pass

