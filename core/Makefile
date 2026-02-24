# Trình biên dịch và cờ (flags)
CC = gcc
CFLAGS = -Wall -Wextra -O2 -Iinclude -fPIC
LDFLAGS = -lm

# Thư mục
SRC_DIR = src
OBJ_DIR = obj
INC_DIR = include

# Tên file thực thi và thư viện
TARGET = wing_test
LIB_TARGET = libwingcore.so

# Tự động thu thập tất cả file nguồn trong thư mục src, nhưng loại trừ test_bench.c
# Điều này đảm bảo các hàm tiện ích (constants.c, aeroCore.c, weightCore.c, ...) được
# biên dịch vào thư viện lõi.
CORE_SRCS = $(filter-out $(SRC_DIR)/test_bench.c,$(wildcard $(SRC_DIR)/*.c))
TEST_SRC = $(SRC_DIR)/test_bench.c

# Chuyển đổi sang file object tương ứng
CORE_OBJS = $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(CORE_SRCS))
TEST_OBJ = $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(TEST_SRC))

all: $(TARGET) lib

# Quy tắc build file chạy test (Liên kết test_bench với lõi tính toán)
$(TARGET): $(TEST_OBJ) $(CORE_OBJS)
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)
	@echo "--- Đã biên dịch xong công cụ kiểm tra $(TARGET) ---"

# Quy tắc build thư viện sạch cho Flying Wing
# Thư viện này chỉ chứa logic tính toán, không chứa hàm main() của test_bench
lib: $(CORE_OBJS)
	$(CC) -shared -o $(LIB_TARGET) $^ $(LDFLAGS)
	@echo "--- Đã tạo thư viện lõi $(LIB_TARGET) ---"

# Quy tắc biên dịch file .o
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(OBJ_DIR):
	mkdir -p $(OBJ_DIR)

clean:
	rm -rf $(OBJ_DIR) $(TARGET) $(LIB_TARGET)
	@echo "--- Đã dọn dẹp các tệp tin Flying Wing ---"

.PHONY: all lib clean