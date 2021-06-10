make

PROG_FILE=$(ls build/*.elf | head -1) #Create an environment variable 

openocd "-f" "interface/stlink-v2-1.cfg" "-f" "target/stm32f4x.cfg" "-c" "program ${PROG_FILE} verify reset exit"
