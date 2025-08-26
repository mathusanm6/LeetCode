# =============================================================================
# Project Configuration
# =============================================================================

# Compiler and Linker
CXX = clang++

# Directories
COMMON_DIR = common
PROBLEMS_DIR = problems

# Python settings
PYTHON = python3
PYTEST = pytest

# =============================================================================
# Compiler and Linker Flags
# =============================================================================

# Google Test library path
GTEST_LIB_PATH = -I$(shell brew --prefix googletest)/include
GTEST_LINK_PATH = -L$(shell brew --prefix googletest)/lib

# CXXFLAGS: C++20 standard, all warnings, warning pedantic mode, include common and problems directories
CXXFLAGS = -std=c++20 -Wall -Wextra -Wpedantic -I$(COMMON_DIR) -I$(PROBLEMS_DIR) $(GTEST_LIB_PATH)

# LDFLAGS
TEST_LDFLAGS = $(GTEST_LINK_PATH) -lgtest -lgtest_main -pthread
DEBUG_LDFLAGS = -g -DDEBUG

# =============================================================================
# File Discovery
# =============================================================================

# Find all problem directories and extract their names (snake_case)
PROBLEM_DIRS = $(wildcard $(PROBLEMS_DIR)/*)
SNAKE_CASE_PROBLEM_NAMES = $(notdir $(PROBLEM_DIRS))

# Find all cpp source files
COMMON_SRCS = $(wildcard $(COMMON_DIR)/*.cc)
PROBLEM_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(filter-out $(dir)/*_test.cc,$(wildcard $(dir)/*.cc)))
PROBLEM_TEST_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(wildcard $(dir)/*_test.cc))

# Find all python test files
PYTHON_TEST_SRCS = $(wildcard $(PROBLEMS_DIR)/*_test.py)

# =============================================================================
# Main Build Rules
# =============================================================================

# =============================================================================
# Test Rules
# =============================================================================

.PHONY: test-cpp\:%
test-cpp\:%:
	@if [ "$*" = "all" ]; then \
		echo "Running C++ tests..."; \
		echo ""; \
		for dir in $(PROBLEM_DIRS); do \
			if [ -f $$dir/*_test.cc ]; then \
				echo "Testing C++ in $$dir..."; \
				$(CXX) $(CXXFLAGS) $(DEBUG_LDFLAGS) $(TEST_LDFLAGS) -I$(COMMON_DIR) -I$$dir -o $$dir/test_runner $$dir/*.cc; \
				if [ $$? -eq 0 ]; then \
					cd $$dir && ./test_runner --gtest_brief=1 --gtest_color=yes 2>/dev/null | tail -n +2; \
					rm -f $$dir/test_runner; \
				else \
					echo "Failed to compile tests in $$dir"; \
				fi; \
				if [ "$$dir" != "$(lastword $(PROBLEM_DIRS))" ]; then \
					echo ""; \
				fi; \
			fi; \
		done; \
	else \
		snake_case_name=$(call kebab_to_snake,$*); \
		if [ -f $(PROBLEMS_DIR)/$$snake_case_name/$${snake_case_name}_test.cc ]; then \
			echo "Running C++ tests for $*..."; \
			$(CXX) $(CXXFLAGS) $(DEBUG_LDFLAGS) $(TEST_LDFLAGS) -I$(COMMON_DIR) -I$(PROBLEMS_DIR)/$$snake_case_name -o $(PROBLEMS_DIR)/$$snake_case_name/test_runner $(PROBLEMS_DIR)/$$snake_case_name/*.cc; \
			if [ $$? -eq 0 ]; then \
				cd $(PROBLEMS_DIR)/$$snake_case_name && ./test_runner --gtest_color=yes 2>/dev/null | tail -n +2; \
				rm -f $(PROBLEMS_DIR)/$$snake_case_name/test_runner; \
			else \
				echo "Failed to compile tests for $*"; \
			fi; \
		fi; \
	fi

.PHONY: test-py\:%
test-py\:%:
	@if [ "$*" = "all" ]; then \
		echo "Running Python tests..."; \
		echo ""; \
		for dir in $(PROBLEM_DIRS); do \
			if [ -f $$dir/*_test.py ]; then \
				cd $$dir && $(PYTEST) *_test.py --color=yes 2>/dev/null | tail -n +7; \
				cd - > /dev/null; \
			fi; \
		done; \
	else \
		snake_case_name=$(call kebab_to_snake,$*); \
		if [ -f $(PROBLEMS_DIR)/$$snake_case_name/$${snake_case_name}_test.py ]; then \
			echo "Running Python tests for $*..."; \
			cd $(PROBLEMS_DIR)/$$snake_case_name && $(PYTEST) $${snake_case_name}_test.py -v --color=yes 2>/dev/null | tail -n +7; \
		else \
			echo "No Python test file found for $*."; \
		fi; \
	fi

# =============================================================================
# Compilation Rules
# =============================================================================

# =============================================================================
# Utility Rules
# =============================================================================

# Converter from snake_case to kebab-case
define kebab_to_snake
$(subst -,_,$(1))
endef