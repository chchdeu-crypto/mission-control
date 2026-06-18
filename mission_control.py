#mission 1/2
agent_name = "chaim"
mission_code = 2144
distance_to_target = 100.0
mission_active_status = True
#mission 3
print(agent_name)
print(mission_code)
print(distance_to_target)
print(mission_active_status)
#mission 4
print("agent var type",type(agent_name))
print("mission code var type" ,type(mission_code))
print("distance var type" ,type(distance_to_target))
print("mission_active_var", type(mission_active_status))
#mission 5
full_distance = distance_to_target*2
print("the pull distance", full_distance)
#mission 6
fuel_usage = 2
fuel_usage = int(fuel_usage)
full_fuel_gas = full_distance*fuel_usage
print("full fuel gas", full_fuel_gas)
#mission 7
total_fuel = 450
total_fuel = int(total_fuel)
fuel_remaining = total_fuel-full_fuel_gas
print("fuel remaining" , fuel_remaining)
#mission 8
time_in_second = int(input("enter time in second"))
time_in_minute = time_in_second/60
time_in_hours = time_in_minute/60
print("travel time" , time_in_hours)