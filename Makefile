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
PROBLEM_TEST_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(wildcard $(dir)/*_test.cc))
PROBLEM_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(filter-out $(PROBLEM_TEST_SRCS),$(wildcard $(dir)/*.cc)))

# Find all python test files
PYTHON_TEST_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(wildcard $(dir)/*_test.py))
PYTHON_SRCS = $(foreach dir,$(PROBLEM_DIRS),$(filter-out $(PYTHON_TEST_SRCS),$(wildcard $(dir)/*.py)))

# =============================================================================
# Test Rules
# =============================================================================

# Converter from snake_case to kebab-case
define kebab_to_snake
$(subst -,_,$(1))
endef

.PHONY: test\:%
test\:%:
	@make test-cpp:$* 
	@echo ""
	@make test-py:$*

.PHONY: test-cpp\:%
test-cpp\:%:
	@if [ "$*" = "all" ]; then \
		echo "Running all C++ tests..."; \
		for dir in $(PROBLEM_DIRS); do \
			if [ -f $$dir/*_test.cc ]; then \
				echo "$(call color_blue,Testing C++ in $$dir...)"; \
				$(CXX) $(CXXFLAGS) $(DEBUG_LDFLAGS) $(TEST_LDFLAGS) -I$(COMMON_DIR) -I$$dir -o $$dir/test_runner $$dir/*.cc; \
				if [ $$? -eq 0 ]; then \
					cd $$dir && ./test_runner --gtest_brief=1 --gtest_color=yes 2>/dev/null | tail -n +2; \
					rm -f $$dir/test_runner; \
				else \
					echo "$(call color_red,Failed to compile tests in $$dir)"; \
				fi; \
				if [ "$$dir" != "$(lastword $(PROBLEM_DIRS))" ]; then \
					echo ""; \
				fi; \
			fi; \
		done; \
	else \
		snake_case_name=$(call kebab_to_snake,$*); \
		if [ -f $(PROBLEMS_DIR)/$$snake_case_name/$${snake_case_name}_test.cc ]; then \
			echo "$(call color_blue,Running C++ tests for $*...)"; \
			$(CXX) $(CXXFLAGS) $(DEBUG_LDFLAGS) $(TEST_LDFLAGS) -I$(COMMON_DIR) -I$(PROBLEMS_DIR)/$$snake_case_name -o $(PROBLEMS_DIR)/$$snake_case_name/test_runner $(PROBLEMS_DIR)/$$snake_case_name/*.cc; \
			if [ $$? -eq 0 ]; then \
				cd $(PROBLEMS_DIR)/$$snake_case_name && ./test_runner --gtest_color=yes 2>/dev/null | tail -n +2; \
				rm -f $(PROBLEMS_DIR)/$$snake_case_name/test_runner; \
			else \
				echo "$(call color_red,Failed to compile tests for $*)"; \
			fi; \
		fi; \
	fi
	@make clean SILENT=true

.PHONY: test-py\:%
test-py\:%:
	@if [ "$*" = "all" ]; then \
		echo "Running all Python tests..."; \
		for dir in $(PROBLEM_DIRS); do \
			if [ -f $$dir/*_test.py ]; then \
				cd $$dir && $(PYTEST) *_test.py --color=yes 2>/dev/null | tail -n +7; \
				cd - > /dev/null; \
			fi; \
		done; \
	else \
		snake_case_name=$(call kebab_to_snake,$*); \
		if [ -f $(PROBLEMS_DIR)/$$snake_case_name/$${snake_case_name}_test.py ]; then \
			echo "$(call color_blue,Running Python tests for $*...)"; \
			cd $(PROBLEMS_DIR)/$$snake_case_name && $(PYTEST) $${snake_case_name}_test.py -v --color=yes 2>/dev/null | tail -n +8; \
		else \
			echo "$(call color_red,No Python test file found for $*.)"; \
		fi; \
	fi
	@make clean SILENT=true

# =============================================================================
# Code Quality Rules
# =============================================================================

.PHONY: format
format:
	@make format-cpp
	@echo ""
	@make format-python

.PHONY: format-cpp
format-cpp:
	@echo "Formatting C++ files..."
	@if command -v clang-format >/dev/null 2>&1; then \
		find $(COMMON_DIR) $(PROBLEMS_DIR) -name '*.cc' -o -name '*.h' | xargs clang-format -i; \
		echo "$(call color_green,C++ files formatted.)"; \
	else \
		echo "$(call color_red,clang-format not found. Please install it to format C++ files.)"; \
	fi

.PHONY: format-python
format-python:
	@echo "Formatting Python files..."
	@if command -v ruff >/dev/null 2>&1; then \
		ruff format $(PROBLEMS_DIR); \
		echo "$(call color_green,Python files formatted with ruff.)"; \
	elif command -v black >/dev/null 2>&1; then \
		find $(PROBLEMS_DIR) -name '*.py' | xargs black; \
		echo "$(call color_green,Python files formatted with black.)"; \
	else \
		echo "$(call color_red,Neither ruff nor black found. Please install one of them to format Python files.)"; \
	fi

.PHONY: lint
lint:
	@make lint-cpp
	@echo ""
	@make lint-python

.PHONY: lint-cpp
lint-cpp:
	@echo "Linting C++ files..."
	@if command -v clang-tidy >/dev/null 2>&1; then \
		find $(PROBLEMS_DIR) $(COMMON_DIR) -type f \( -name '*.cc' -o -name '*.h' \) | while read -r file; do \
			clang-tidy "$$file" -- $(CXXFLAGS) -x c++ || true; \
		done; \
		echo "$(call color_green,C++ linting complete.)"; \
	else \
		echo "$(call color_red,clang-tidy not found. Please install it to lint C++ files.)"; \
	fi

.PHONY: lint-python
lint-python:
	@echo "Linting Python files..."
	@if command -v ruff >/dev/null 2>&1; then \
		ruff check $(PROBLEMS_DIR); \
		echo "$(call color_green,Python linting complete with ruff.)"; \
	elif command -v flake8 >/dev/null 2>&1; then \
		find $(PROBLEMS_DIR) -name '*.py' | xargs flake8; \
		echo "$(call color_green,Python linting complete with flake8.)"; \
	else \
		echo "$(call color_red,Neither ruff nor flake8 found. Please install one of them to lint Python files.)"; \
	fi

# =============================================================================
# Utility Rules
# =============================================================================

.PHONY: clean
clean:
	@if [ "$(SILENT)" != "true" ]; then \
		echo "Cleaning build artifacts..."; \
	fi
	@find $(PROBLEMS_DIR) -type f -executable -not -name "*.py" -not -name "*.cc" -not -name "*.h" -delete 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name "test_runner" -delete 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name "test_runner.dSYM" -type d -exec rm -rf {} + 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name "*_debug" -delete 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name "*.pyc" -delete 2>/dev/null || true
	@find $(PROBLEMS_DIR) -name ".pytest_cache" -type d -exec rm -rf {} + 2>/dev/null || true
	@if [ "$(SILENT)" != "true" ]; then \
		echo "$(call color_green,Clean complete.)"; \
	fi

# Show project statistics
.PHONY: stats
stats:
	@echo "=== Project Statistics ==="
	@echo "$(call color_green,Problems found:) $(words $(SNAKE_CASE_PROBLEM_NAMES))"
	@echo "$(call color_green,C++ sources:) $(words $(COMMON_SRCS) $(PROBLEM_SRCS))"
	@echo "$(call color_green,C++ tests:) $(words $(PROBLEM_TEST_SRCS))"
	@echo "$(call color_green,Python sources:) $(words $(PYTHON_SRCS))"
	@echo "$(call color_green,Python tests:) $(words $(PYTHON_TEST_SRCS))"
	@echo ""
	@echo "Available problems:"
	@for prob in $(SNAKE_CASE_PROBLEM_NAMES); do echo "  $(call color_cyan,- $$prob)"; done

# =============================================================================
# Help and Documentation
# =============================================================================

.PHONY: help
help:
	@echo "$(call color_blue,=== LeetCode Project Help ===)"
	@echo ""
	@echo "$(call color_yellow,Test Targets:)"
	@echo "  test-cpp:all       		- Run all C++ tests"
	@echo "  test-cpp:PROBLEM   		- Run C++ tests for specific problem (kebab-case)"
	@echo "  test-py:all        		- Run all Python tests"
	@echo "  test-py:PROBLEM    		- Run Python tests for specific problem (kebab-case)"
	@echo ""
	@echo "$(call color_yellow,Code Quality Targets:)"
	@echo "  format             		- Format all code (C++ and Python)"
	@echo "  format-cpp         		- Format C++ code only"
	@echo "  format-python      		- Format Python code only"
	@echo "  lint               		- Lint all code (C++ and Python)"
	@echo "  lint-cpp           		- Lint C++ code only"
	@echo "  lint-python        		- Lint Python code only"
	@echo ""
	@echo "$(call color_yellow,Utility Targets:)"
	@echo "  clean              		- Clean build artifacts"
	@echo "  stats              		- Show project statistics"
	@echo "  help               		- Show this help message"
	@echo ""
	@echo "$(call color_green,Examples:)"
	@echo "  make test-cpp:two-sum  	- Test C++ solution for two-sum"
	@echo "  make test-py:all       	- Run all Python tests"
	@echo "  make format			- Format all source files"
	@echo ""
	@echo "$(call color_cyan,Available problems:) $(SNAKE_CASE_PROBLEM_NAMES)"

# =============================================================================
# Color Functions
# =============================================================================

# Color definitions
define color_blue
\033[1;34m$(1)\033[0m
endef

define color_green
\033[1;32m$(1)\033[0m
endef

define color_yellow
\033[1;33m$(1)\033[0m
endef

define color_cyan
\033[1;36m$(1)\033[0m
endef

define color_reset
\033[0m
endef