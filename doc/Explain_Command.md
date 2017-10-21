## Config

### Danh tính 

Cấu hình username và email, các thông tin này sẽ gắn vào mỗi lần commit 

```
$ git config --global user.name "Loc VU"
$ git config --global user.email locvx1234@gmail.com
```

Biến `--global` giúp áp dụng thông tin này trên các project của hệ thống, chỉ phải cấu hình 1 lần đầu tiên

### Editor 

Mặc định là Vi hoặc Vim, có thể thay đổi editor bằng lệnh :

```
$ git config --global core.editor emacs
```

### Công cụ so sánh thay đổi 

```
$ git config --global merge.tool vimdiff
```

Các công cụ khác : kdiff3, tkdiff, meld, xxdiff, emerge, vimdiff, gvimdiff, ecmerge, và opendiff

### Kiểm tra cấu hình 

```
$ git config --list
```

## Help

Có 3 cú pháp dùng để tìm kiếm tài liệu của lệnh git

```
$ git help <verb>
$ git <verb> --help
$ man git-<verb>
```

Ví dụ : 

```
$ git help config
```

## Git basic

Khởi tạo một thư mục git 

```
$ git init
```

Tổ chức các tập tin, tạo mới ảnh của các tập tin đó vào khu vực tổ chức

```
$ git add filename
```

Commit, ảnh của các tập tin trong khu vực tổ chức sẽ được lưu trữ vĩnh viễn vào thư mục Git

```
$ git commit -m "commit message"
```

Tips: Thêm tùy chọn `-a` để bỏ qua giai đoạn staged mỗi lần commit 

Sao chép một repository 

```
$ git clone [url]
```

Kiểm tra trạng thái tập tin 

```
$ git status
```

Sự thay đổi của tập tin chưa được staged 

```
$ git diff
```

Sự thay đổi của tập tin đã staged, chuẩn bị commit 

```
$ git diff --staged
``` 

Trước  version 1.6.1 là `git diff --cached`

Xóa tập tin khỏi thư mục staged 

```
$ git rm filename
```

Tips: Sử dụng `-f` chức năng an toàn để đưa ra thông báo xác nhận xóa.

Giữ tập tin trong thư mục làm việc nhưng không thêm vào khu vực tổ chức, ngoài việc thêm vào file `.gitognore`

```
$ git rm --cached readme.txt
```

Di chuyển file 

```
$ git mv file_from file_to
```

## Git log 

Liệt kê các commit đã thực hiện trên repo đó, theo thứ tự commit mới nhất được hiển thị đầu tiên

```
$ git log
```

Một số tùy chọn sử dụng với `git log`

|-------------------|-------------------------------------------------------------------------------------|
|  Tùy chọn         |   Mô tả                                                                             |
|-------------------|-------------------------------------------------------------------------------------|
| `-p`		        | Hiển thị bản vá ở mỗi commit                                                        |
| `--word-dif`      | Hiển thị bản vá ở định dạng tổng quan (word)                                        |
| `--stat`	        | Hiển thị thống kê của các tập tin được chỉnh sửa trong mỗi commit                   |
| `--shortstat`     | 	Chỉ hiển thị thay đổi/thêm mới/xoá bằng lệnh --stat                               |
| `--name-only`     | Hiển thị danh sách các tập tin đã thay đổi sau thông tin của commit                 |
| `--name-status`   | Hiển thị các tập tin bị ảnh hưởng với các thông tin như thêm mới/sửa/xoá            |
| `--abbrev-commit` | Chỉ hiện thị một số ký tự đầu của mã băm SHA-1 thay vì tất cả 40                    |
| `--relative-date` | Hiển thị ngày ở định dạng tương đối (ví dụ, "2 weeks ago") thay vì định dạng đầy đủ |
| `--graph`		    | Hiển thị biểu đồ ASCII của nhánh và lịch sử tích hợp cùng với thông tin đầu ra khác |
| `--pretty` 	    | Hiện thị các commit sử dụng một định dạng khác. Các lựa chọn bao gồm oneline, short, full, fuller và format (cho phép bạn sử dụng định dạng riêng) |
| `--oneline` 	    | Một lựa chọn ngắn, thuận tiện cho `--pretty=oneline` `--abbrev-commit`              |

 
Giới hạn thông tin đầu ra 

`git log` nhận một số lựa chọn khác cho việc giới hạn thông tin xuất ra 

|---------------------|--------------------------------------------------------------------------|
| Lựa chọn			  | Mô tả												    		   		 |
|---------------------|--------------------------------------------------------------------------|
| `-(n)`			  | Chỉ hiển thị n commit mới nhất                							 |
| `--since, --after`  | Giới hạn các commit được thực hiện sau ngày nhất định					 |
| `--until, --before` | Giới hạn các commit được thực hiện trước ngày nhất định 				 |
| `--author`		  | Chỉ hiện thị các commit mà tên tác giả thoả mãn điều kiện nhất định 	 |
| `--committer`		  |	Chỉ hiện thị các commit mà tên người commit thoả mãn điều kiện nhất định |










