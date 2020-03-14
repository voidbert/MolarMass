# MolarMass
A Python script for the CASIO fx-CG50 that calculates the molar mass of a substance. It was made with MicroPython in mind but it also runs on any Python 3 interpreter. I was tired of calculating molar masses for chemistry exercises by hand and I decided to make this program.

### Usage

For normal molecules and ionic substances, you can input their formula directly. Be aware that you will still need to use upper and lower case letters for the atoms. Example: `NaBrO3`. Note that, due to the lack of subscript characters in the calculator, numbers must be written as normal text.

Due to the lack of the middle dot character (`·`) used to write the formulas of hydrates, the dot (`.`) character is used in its place. Also, the number of water molecules in hemi and sesqui hydrates must be written as a decimal number, for example: `CaSO4.0.5H2O`

For some reason, you can't use the `EXIT` key while CASIO's Python interpreter is inside a while loop, at least in my version of the calculator. If you want to exit the script, you can write `EXIT` (case-insensitive) in the place you insert molecules. The `AC` key should terminate the script but I'm not sure if that works on every version of the calculator.
