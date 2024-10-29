CXX = clang++
CXXFLAGS = -std=c++17 -Wall -Wextra -Werror -g
PROBLEM_DIR = problems
TEST_DIR = tests
BUILD_DIR = build

# Colors for output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[1;34m
NC = \033[0m  # No Color

# Create build directory structure if it doesn't exist
$(shell mkdir -p $(BUILD_DIR))
$(shell find $(PROBLEM_DIR) -type d | sed 's|^$(PROBLEM_DIR)|$(BUILD_DIR)|' | xargs -I {} mkdir -p {})
$(shell find $(TEST_DIR) -type d | sed 's|^$(TEST_DIR)|$(BUILD_DIR)|' | xargs -I {} mkdir -p {})

# Find all .cpp files in problems and tests subdirectories (recursively)
PROBLEM_SRCS := $(shell find $(PROBLEM_DIR) -name "*.cpp")
TEST_SRCS := $(filter-out $(TEST_DIR)/test.cpp, $(shell find $(TEST_DIR) -name "*.cpp"))
MAIN_SRC := $(TEST_DIR)/test.cpp

# Convert source file paths to object file paths in the build directory
PROBLEM_OBJS := $(patsubst $(PROBLEM_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(PROBLEM_SRCS))
TEST_OBJS := $(patsubst $(TEST_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(TEST_SRCS))
MAIN_OBJ := $(BUILD_DIR)/test.o

# Target to build all tests
all: $(BUILD_DIR)/tests

# Compile each problem .cpp file to a .o file in the build directory
$(BUILD_DIR)/%.o: $(PROBLEM_DIR)/%.cpp
	@echo "$(YELLOW)Compiling $<...$(NC)"
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Compile each test .cpp file to a .o file in the build directory
$(BUILD_DIR)/%.o: $(TEST_DIR)/%.cpp
	@echo "$(YELLOW)Compiling $<...$(NC)"
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Compile the main file separately
$(MAIN_OBJ): $(MAIN_SRC)
	@echo "$(YELLOW)Compiling main file $<...$(NC)"
	$(CXX) $(CXXFLAGS) -c -o $@ $<

# Link all object files to create the test executable
$(BUILD_DIR)/tests: $(PROBLEM_OBJS) $(TEST_OBJS) $(MAIN_OBJ)
	@echo "$(GREEN)Linking all tests...$(NC)"
	$(CXX) $(CXXFLAGS) -o $@ $^

# Run tests
run_tests: $(BUILD_DIR)/tests
	@echo "$(GREEN)Running all tests...$(NC)"
	@$(BUILD_DIR)/tests

# Formatting
format:
	@echo "$(BLUE)Formatting C++ files...$(NC)"
	@clang-format -i $(PROBLEM_SRCS) $(TEST_SRCS) $(MAIN_SRC)
	@echo "$(GREEN)Formatting completed.$(NC)"

# Clean build artifacts
clean:
	@echo "$(RED)Cleaning build artifacts...$(NC)"
	@rm -rf $(BUILD_DIR)/*
	@echo "$(GREEN)Clean completed.$(NC)"

.PHONY: all run_tests clean format
