file=open('ms.txt')
file1=file.readlines()

x=[-42.0, 162.0, -31.0, -73.0, 48.0, -112.0, 4.0, 200.0, -1.0, -122.0, -26.0, -123.0, -142.0, -50.0, 111.0, -67.0, 40.0, -33.0, -3.0, -45.0, -197.0, -72.0, -159.0, -224.0, -23.0, -126.0, -233.0, -155.0, -176.0, -218.0, 44.0, -80.0, -132.0, 93.0, 122.0, -105.0]
y=[-160.0, 13.0, -198.0, -138.0, 48.0, -200.0, -87.0, 118.0, -159.0, -163.0, -134.0, -126.0, -69.0, -124.0, 38.0, -166.0, 133.0, 43.0, 106.0, 145.0, 96.0, -78.0, -29.0, -141.0, -38.0, 25.0, -101.0, -100.0, -78.0, -47.0, -14.0, -192.0, 173.0, -73.0, 132.0, 115.0]
states=['Abia', 'Adamawa', 'Akwaibom', 'Anambra', 'Bauchi', 'Bayelsa', 'Banue', 'Borno', 'Crossriver', 'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe', 'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Kastina', 'Kebbi', 'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun', 'Ondo', 'Osun', 'Oyo', 'Platue', 'Rivers', 'Sokoto', 'Taraba', 'Yobe', 'Zamfara']

state_data={
	"State":states,
	"X":x,
	"Y":y
}
import pandas

nd=pandas.DataFrame(state_data)
nd.to_csv("states_in_nigeria.csv")













