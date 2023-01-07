# Compiler and Linker flags
CC				:= clang++
SRC_DIR			:= src
BIN_DIR			:= $(BIN_DIR)/sfmlgame
BIN_EXE			:= $(if $(findstring Windows_NT, $(OS)), $(BIN_EXE).exe, $(BIN_EXE))
OUTPUT			:= $(BIN_DIR)/obj
INC_DIRS		:= -I$(SRC_DIR) -I$(SFML_DIR)/include
LIB_DIRS		:= -L$(SFML_DIR)/lib
SRC_FILES		:= $(wildcard $(SRC_DIR)/*.cpp)
H_FILES			:= $(wildcard $(SRC_DIR)/*.h)
OBJ_FILES		:= $(patsubst $(SRC_DIR)/%.cpp, $(OBJ_DIR)/%.o, $(SRC_FILES))
CPP_FLAGS		:= -03 -std=c++17
LD_FLAGS		:= -03 -lsfml-graphics -lsfml-window -lsfml-system -lsfml-audio
MAKEFLAGS		+= -j8

# compile the object files and place them in their own directory.
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp %(H_FILES)
	$(CC)	$(CPP_FLAGS) $(INC_DIRS) -c -o $@ $<



# link the object files together to create a final executable.
$(OUTPUT): $(OBJ_FILES) Makefile
	#(CC) $(LIB_DIRS) $(LD_FLAGS) $(OBJ_FILES) -o $(OUTPUT)

# when we type make, compile and link the executable.
all: $(OUTPUT)

# if we type 'make run' it will build and run the executable.
