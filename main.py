# practice

#import math library
import math

import cv2

from prettytable import PrettyTable

#Earth's Gravity in (km/s^2))
g = 9.81 / 1000
Isp = 350 #Isp in seconds

#Dry Mass(kg)
m_f = 32548

#Delta V(km/s)
delta_v = 1.53

#Density of Fuel and Oxidizer(kg/m^3)
row = 1032
row_OX = 1150

#Oxidizer to Fuel Ratio
OF = 2.2

#Thrust to Weight Ratio
T_W = 3

#Wet Mass
m_o = math.exp(delta_v / (g * Isp)) * m_f

#Mass Propellant(kg)
m_prop = (m_o - m_f)*1.05 #(extra propellant added for redundency)

#Mass Fuel(kg)
m_fuel = m_prop * (1 / OF)

#Mass Oxidizer(kg)
m_OX = m_prop - m_fuel
V_fuel = m_fuel / row
V_OX = m_OX / row_OX


#Stresses and FOS

#Yield yield,ultimate strength, and modulus of elasticity of Materials(Al 6061-T6)(Kpa)
Fy = 241317
Fu = 310264
E = 68948000
#Maximum allowable operating pressure(use lower of two for calcs)
SW = Fy/1.25 #Denominator is a FOS
SW2 = Fu/1.5
#Weld efficiency(assumed perfected @ ew = 1)
ew = 1

#Radius of the tank and spherical section(m)
r_s = .72

#Operation Pressure(Kpa)
P_t= 6200

#Density of Tank Material Al-6061 T6(kg/m^3)
dens = 2710

#Fuel Tank Needed Volume
T_fuel  = .015 * V_fuel                            #Trapped Propellant Volume
B_fuel = 0                                         #Boil Off Volume
U_per_fuel = .02                                   #Ullage percent
U_vol_fuel =(V_fuel + T_fuel) * U_per_fuel         #Ullage Volume
V_total_rec_fuel = V_fuel + T_fuel + B_fuel + U_vol_fuel   #Total Propellant Tank Volume Recommended for assumed values

#Spherical End Calculations
#Note: SW is used because yield strength is always lower than ultimate strength
Vs_f = (2*math.pi*pow(r_s,3))/3 #Volume(m^3)
t_k = (.5*P_t*r_s)/(2*SW)       #Thickness of knuckle(m)
t_cr = (P_t*.7)/(2*SW*ew)       #Thickness of crown(m)


#Equivalent wall thickness of a spherical tank-end(m)
ts = (P_t*r_s)/(2*SW*ew)

#Spherical Tank End Weight (kg)
W_S = 2*math.pi*pow(r_s,2)*ts*dens

#Cylindrical Section
l_cyl = 2                  #length of the cylindrical section(m)
V_cyl= math.pi*pow(r_s,2)*l_cyl #Volume of the cylindrical section(m^3)
V_total_fuel = V_cyl+(2*Vs_f)   #Total Volume(m^3)

#Wall thickness of Cylindrical Tank(m)
tc_fuel = (P_t * r_s)/(SW*ew)
#Weight of cylindrical section(kg)
W_cyl = 2*math.pi*r_s*l_cyl*tc_fuel*dens
#Total Weight of Fuel Tank(kg)
tot_w_f = W_cyl+(2*W_S)


#Critical Pressure due to external loading(Kpa)
Pcrs_fuel = (.342*E*pow(ts,2))/pow(r_s,2)
#Hoop and Axial Stress for fuel tank(Kpa)
sigma_hoop_fuel = (P_t*r_s)/tc_fuel
sigma_fuel = (P_t*r_s)/(2*tc_fuel)


#Oxidizer Tanks

#Oxidizer Tank Needed Volumem^3)
T_OX  = .01 * V_OX                 #Trapped Propellant Volume
B_OX =  .02 * V_OX                              #Boil Off Volume
U_per_OX = .02                              #Ullage percent
U_vol_OX =(V_OX + T_OX) * U_per_OX         #Ullage Volume
V_total_rec_OX = V_OX + T_OX + B_OX + U_vol_OX #Total Propellant Tank Volume Recommended for assumptions

#Radius of the tank and spherical section(m)
r_s_OX = .72

#Operation Pressure(Kpa)
P_t_OX= 6200

#Density of Tank Material Al-6061 T6(kg/m^3)
dens_OX = 2710

#Spherical End Calculations
Vs_OX = (2*math.pi*pow(r_s,3))/3 #Volume(m^3)
t_k_OX = (.5*P_t_OX*r_s_OX)/(2*SW)       #Thickness of knuckle(m)
t_cr_OX = (P_t_OX*.7)/(2*SW*ew)       #Thickness of crown(m)


#Equivalent wall thickness of a spherical tank-end(m)
ts_OX = (P_t_OX*r_s_OX)/(2*SW*ew)

#Spherical Tank End Weight (kg)
W_S_OX = 2*math.pi*pow(r_s_OX,2)*ts_OX*dens


#Cylindrical Section
l_cyl_OX = 2                    #length of the cylindrical section(m)
V_cyl_OX = math.pi*pow(r_s,2)*l_cyl_OX #Volume of the cylindrical section(m^3)
V_total_OX = V_cyl_OX+(2*Vs_OX)   #Total Volume(m^3)

#Wall thickness of Cylindrical Tank(m)
tc_OX = (P_t_OX * r_s_OX)/(SW*ew)
#Weight of cylindrical section(kg)
W_cyl_OX = 2*math.pi*r_s_OX*l_cyl_OX*tc_OX*dens
#Total Weight of Fuel Tank(kg)
tot_w_OX = W_cyl_OX+(2*W_S)


#Critical Pressure due to external loading(Kpa)
Pcrs_OX = (.342*E*pow(ts,2))/pow(r_s,2)
#Hoop and Axial Stresses for OX tank(Kpa)
sigma_hoop_OX = (P_t*r_s)/tc_OX
sigma_OX = (P_t*r_s)/(2*tc_OX)



# These 3 are the columns of the tables
t = PrettyTable(['Dimension', 'Fuel(Hydrazine)','Oxidizer(LoX)'])

# To insert rows:
t.add_row(['Propellant Volume(m^3)', f"{V_fuel:.2f}", f"{V_OX:.2f}"])
t.add_row(['Propellant Mass(kg)', f"{m_fuel:.2f}",f"{m_OX:.2f}"],divider=True)
t.add_row(['Recommended Tank Volume (m^3)', f"{V_total_rec_fuel:.2f}", f"{V_total_rec_OX:.2f}"])
t.add_row(['Actual Tank Volume (m^3)', f"{V_total_fuel:.2f}", f"{V_total_OX:.2f}"])
t.add_row(['Tank Weight(kg)', f"{tot_w_f:.2f}", f"{tot_w_OX:.2f}"],divider=True)
t.add_row(['Volume Spherical Section(m^3)', f"{Vs_f:.2f}",f"{Vs_OX:.2f}"])
t.add_row(['Knuckle Wall Thickness(m)', f"{t_k:.3f}", f"{t_k_OX:.3f}"])
t.add_row(['Crown Wall Thickness(m)', f"{t_cr:.3f}",f"{t_cr_OX:.3f}"])
t.add_row(['Weight(kg)', f"{W_S:.2f}",f"{W_S_OX:.2f}"],divider=True)
t.add_row(['Volume Cylindrical Section(m^3)', f"{V_cyl:.2f}",f"{V_cyl_OX:.2f}"])
t.add_row(['Length(m)', f"{l_cyl:.2f}",f"{l_cyl_OX:.2f}"])
t.add_row(['Thickness(m)', f"{tc_fuel:.3f}",f"{tc_OX:.3f}"],divider=True)
t.add_row(['Operational Pressure(KPa)', f"{P_t:.2f}", f"{P_t_OX:.2f}"])
t.add_row(['Critical External Pressure(KPa)', f"{Pcrs_fuel:.2f}", f"{Pcrs_OX:.2f}"],)
t.add_row(['Hoops Stress(KPa)', f"{sigma_hoop_fuel:.2f}", f"{sigma_hoop_OX:.2f}"])
t.add_row(['Axial Stress(KPa)', f"{sigma_fuel:.2f}", f"{sigma_OX:.2f}"],)
print(t)

#Displays Diagram for tank dimensions and features
img = cv2.imread('Propellant_Tank_Diagram.png')
cv2.imshow('IMAGE', img)
cv2.waitKey(0) #Image goes away X amount of seconds
cv2.imwrite('Tank_Diagram.png',img) #Writes the image to the program