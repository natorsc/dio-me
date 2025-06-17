package main

import "fmt"

const ebulicaoKelvin = 373.0

func main() {
	temperaturaKelvin := ebulicaoKelvin
	temperaturaCelsius := temperaturaKelvin - 273.0
	fmt.Printf("A temperatura de ebulição da água em Kelvin = %g e a temperatura de ebulição da água em °C (Celsius) = %g.", temperaturaKelvin, temperaturaCelsius)
}
