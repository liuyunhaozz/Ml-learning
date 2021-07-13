x = [1000 / (25+273), 1000 / (50+273), 1000 / (70+273), 1000 / (80+273)]

D_1 = [4.11, 4.92, 6.10, 6.66]
D_2 = [4.27, 4.92, 6.14, 6.62]
y_1 = log(D_1)
y_2 = log(D_2)

linreg_1 = LinearModel.fit(x,y_1)
linreg_2 = LinearModel.fit(x,y_2)
linreg_3 = LinearModel.fit([x,x],[y_1,y_2])


pre_x = [2.8;3.4]
pre_y_1 = linreg_1.predict(pre_x)
pre_y_2 = linreg_2.predict(pre_x)
pre_y_3 = linreg_3.predict(pre_x)


xlabel("$1/T(10^{-3}K)$",'interpreter','latex')
ylabel("$lnD(cm^2/s)$",'interpreter','latex')
set(gca,'xtick',2.8:3.4:0.1,'xlabel','1')  
set(gca,'ytick',1.4:2:0.1)  

plot(pre_x,pre_y_1','r--','DisplayName','Group I samples')
hold on;
plot(pre_x,pre_y_2','g:','DisplayName','Group II samples')
hold on;
scatter(x,y_1,'DisplayName','Group I samples')
hold on;
scatter(x,y_2,'^','DisplayName','Group II samples')
hold on;
plot(pre_x,pre_y_3','b-','DisplayName','All samples')
legend




