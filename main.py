import simulation1
import simulation2

try:
    simulation1.main()
    print('Simulation 1 is complete!')
    simulation2.main()
    print('Simulation 2 is complete!')
except Exception as e:
    print('Error: ', e)



