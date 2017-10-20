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

## Git history 

Liệt kê các commit đã thực hiện trên repo đó, theo thứ tự commit mới nhất được hiển thị đầu tiên

```
$ git log
```

Tips: Sử dụng `-p` để hiển thị diff của mỗi lần commit, `-2` để giới hạn 2 commit gần nhất, `--word-diff` cho phép hiển thì sai khác theo dòng 








