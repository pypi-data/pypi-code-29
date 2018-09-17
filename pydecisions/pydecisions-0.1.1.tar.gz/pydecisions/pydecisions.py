"""
Copyright (c) 2018 Balamurali M
Author: Balamurali M
Gmail: balamurali9m@gmail.com
License: MIT
"""

import numpy as np
from scipy import stats
from scipy.optimize import linprog
from sklearn import tree
import graphviz

class finance:
    def npv(self, rate1, val1):
        self.rate1 = rate1        
        self.val1 = val1
        self.npv1 = np.npv(self.rate1,self.val1)
        return self.npv1      

    def fv(self, rate2z, years2z, pmt2z, pv2z):
        self.rate2 = rate2z/12        
        self.np2 = years2z * 12       
        self.pmt2 = pmt2z * -1
        self.pv2 = pv2z * -1
        self.fv1 = np.fv(self.rate2, self.np2, self.pmt2, self.pv2)
        return self.fv1 

    def pv(self, rate3z, years3z, pmt3z, fv3z):
        self.rate3 = rate3z/12        
        self.np3 = years3z * 12       
        self.pmt3 = pmt3z * -1
        self.fv3 = fv3z
        self.pv1 = np.pv(self.rate3, self.np3, self.pmt3, self.fv3)
        return self.pv1 

    def irr(self,input):
        self.irr_input = input            
        self.irr4 = np.irr(self.irr_input)
        return self.irr4 

class evm:
    def __init__(self, evm_a, evm_b, evm_c, evm_d): 
        self.evm_a = evm_a
        self.evm_b = evm_b
        self.evm_c = evm_c
        self.evm_d = evm_d
        self.evm_e = self.evm_a * self.evm_b        
        self.evm_f = self.evm_a * self.evm_c        
 
    def result(self):
        self.evm_g = self.evm_a - self.evm_f        
        self.evm_h = self.evm_d + self.evm_g        
        self.evm_i = self.evm_a - self.evm_h        
        self.evm_j = self.evm_f - self.evm_e          
        self.evm_k = self.evm_f/self.evm_e             
        self.evm_l = self.evm_f - self.evm_d           
        self.evm_m = self.evm_f/self.evm_d              
        if self.evm_m<1:
            self.evm_n = (self.evm_a - self.evm_f) / (self.evm_a - self.evm_d)    
        else:
            self.evm_n = (self.evm_a - self.evm_f) / (self.evm_h - self.evm_d)
        print('ETC, EAC, VAC, SV, SPI, CV, CPI, TCPI')
        return self.evm_g, self.evm_h, self.evm_i, self.evm_j, self.evm_k, self.evm_l, self.evm_m, self.evm_n

class dar:                             
     def result (self, dar_a, dar_b):
         self.dar_a = dar_a
         self.dar_b = dar_b
         self.dar_val1 = 0
         self.dar_val2 = 0
         self.dar_len = len(self.dar_a)
         for i in range(self.dar_len):
             self.dar_val1 += self.dar_a[i]
             self.dar_val2 += self.dar_b[i]
         if (self.dar_val1 > self.dar_val2):
             self.dar_pr = 'Alternative 1 score is higher than Alternative 2 score'
         elif (self.dar_val1 < self.dar_val2):
             self.dar_pr = 'Alternative 2 score is higher than Alternative 1 score'
         else:
             self.dar_pr = 'Alternative 1 and Alternative 2 scores are the same'
         print (self.dar_pr)
         print('The scores are:')
         return self.dar_val1, self.dar_val2    

class bayes:                              
     def result(self, pa, pb, lk):    
         self.pa = pa                    
         self.pb = pb                    
         self.lk = lk                    
         self.post = (self.lk * self.pa)/self.pb
         return self.post

class slr:
     def result(self, o_x, o_y, o_xp):
         self.o_rmse = 0
         self.o_rmse1 = 0
         self.o_sst = 0
         self.o_ssr = 0
         self.o_num = 0
         self.o_den = 0                
         self.o_x = o_x
         self.o_y = o_y
         self.o_xp = o_xp
         self.o_len = len(self.o_x )
         self.o_x_mean = np.mean(self.o_x)
         self.o_y_mean = np.mean(self.o_y)

         for i in range(self.o_len):
             self.o_num += (self.o_x[i] - self.o_x_mean) * (self.o_y[i] - self.o_y_mean)
             self.o_den += (self.o_x[i] - self.o_x_mean) ** 2
         self.o_b1 = self.o_num / self.o_den
         self.o_b0 = self.o_y_mean - (self.o_b1 * self.o_x_mean)
         
         for i in range(self.o_len):
             self.o_ypred = self.o_b0 + self.o_b1 * self.o_x[i]
             self.o_rmse1 += (self.o_y[i] - self.o_ypred) ** 2
             self.o_sst += (self.o_y[i] - self.o_y_mean) ** 2
             self.o_ssr += (self.o_y[i] - self.o_ypred ) ** 2
             
         self.o_rmse = np.sqrt(self.o_rmse1/self.o_len)
         self.o_r2 = 1 - (self.o_ssr/self.o_sst)
         self.o_yp = self.o_b0 + self.o_b1 * self.o_xp
         print("rmse, r2, predicted")
         return self.o_rmse, self.o_r2, self.o_yp     

class statistics:                             
     def tt1(self, tt1_a, tt1_pmean):
         self.tt1_a = tt1_a
         self.tt1_pmean = tt1_pmean             
         self.tt1_result0 = stats.ttest_1samp(self.tt1_a, self.tt1_pmean, axis=0, nan_policy='propagate')
         return self.tt1_result0 
     
     def ttind(self, ttind_a, ttind_b):
         self.ttind_a = ttind_a
         self.ttind_b = ttind_b            
         self.ttind_result1 = stats.ttest_ind(self.ttind_a, self.ttind_b, equal_var=True, nan_policy='propagate')
         return self.ttind_result1     

     def ttinds(self, ttinds_mn1, ttinds_sd1, ttinds_obs1, ttinds_mn2, ttinds_sd2, ttinds_obs2):
         self.ttinds_mn1 = ttinds_mn1
         self.ttinds_sd1 = ttinds_sd1
         self.ttinds_obs1 = ttinds_obs1 
         self.ttinds_mn2 = ttinds_mn2
         self.ttinds_sd2 = ttinds_sd2
         self.ttinds_obs2 = ttinds_obs2          
         self.ttinds_result2 = stats.ttest_ind_from_stats(self.ttinds_mn1, self.ttinds_sd1, self.ttinds_obs1, self.ttinds_mn2, self.ttinds_sd2, self.ttinds_obs2, equal_var=True)
         return self.ttinds_result2   
        
     def ttrel(self, ttrel_a, ttrel_b):
         self.ttrel_a = ttrel_a
         self.ttrel_b = ttrel_b            
         self.ttrel_result3 = stats.ttest_rel(self.ttrel_a, self.ttrel_b, axis=0, nan_policy='propagate')
         return self.ttrel_result3  

     def chi(self, chi_obs):     
         self.chi_obs = chi_obs
         self.chi_result = stats.chisquare(self.chi_obs, f_exp=None, ddof=0, axis=0)
         return self.chi_result

     def mwu(self, mwu_x, mwu_y):     
         self.mwu_x = mwu_x
         self.mwu_y = mwu_y
         self.mwu_result = stats.mannwhitneyu(self.mwu_x, self.mwu_y, use_continuity=True, alternative=None)
         return self.mwu_result
      
     def rnks(self, rnks_x, rnks_y):     
         self.rnks_x = rnks_x
         self.rnks_y = rnks_y
         self.rnks_result = stats.ranksums(self.rnks_x, self.rnks_y)
         return self.rnks_result   
     
     def wilcx(self, wilcx_x):     
         self.wilcx_x = wilcx_x    
         self.wilcx_result = stats.wilcoxon(self.wilcx_x, y=None, zero_method='wilcox',correction=False)
         return self.wilcx_result 

class linprg:
     def result(self, lp_c, lp_A, lp_b, lp_x0b, lp_x1b):
         self.lp_c = lp_c
         self.lp_A = lp_A              
         self.lp_b = lp_b
         self.lp_x0b = lp_x0b
         self.lp_x1b = lp_x1b
         self.lp_result = linprog(self.lp_c, A_ub=self.lp_A, b_ub=self.lp_b, bounds=(self.lp_x0b, self.lp_x1b), options={"disp": True})
         return self.lp_result 

class mc:
     def result(self, t_mar, i_mar, n_mar):
         self.t_mar = t_mar
         self.i_mar = i_mar
         self.n_mar = n_mar
         self.t_mar_n = np.linalg.matrix_power(self.t_mar, self.n_mar)
         return self.i_mar * self.t_mar_n

class DTr:
     def result(self, x, y, z):  
        self.x = x
        self.y = y
        self.z = z
        clr = tree.DecisionTreeRegressor()
        clr = clr.fit(self.x, self.y)
        inp = tree.export_graphviz(clr, out_file=None) 
        g1 = graphviz.Source(inp) 
        g1.render("rdiagram")
        with open("rdiagram.dot", "w") as f:
             inp = tree.export_graphviz(clr, out_file=f, 
                             filled=True, rounded=True,  
                             special_characters=True) 
        print (clr.predict(self.z))

class DTc:
     def result(self, x, y, z):  
        self.x = x
        self.y = z
        self.z = z
        cls = tree.DecisionTreeClassifier()
        cls = cls.fit(x, y)
        inp = tree.export_graphviz(cls, out_file=None) 
        g1 = graphviz.Source(inp) 
        g1.render("cdiagram")
        with open("cdiagram.dot", "w") as f:
             inp = tree.export_graphviz(cls, out_file=f, 
                             filled=True, rounded=True,  
                             special_characters=True) 
        print(cls.predict(self.z))
        

