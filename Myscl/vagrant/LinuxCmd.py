'''
1. ls (list segments) : 현재 위치의 파일 목록 조회
ls -l : 파일의 상세정보
ls -a : 숨김 파일 표시
ls -t : 파일 생성 시간순(최신순)으로 표시
ls -rt : 파일들 생성 시간순( 제일 오래된것부터)으로 표시

2, cd (Change directory) : 디렉터리 이동
cd 다텍터리 경로 : 이동하려는 디렉터리로 이동
cd ~ : 홈 디렉터리로 이동
cd / : 최상위 디렉터리로 이동
cd . : 현재 디렉터리
cd .. : 상위 디렉터리로 이동
cd - : 이전 경로로 이동

3. touch : 0바이트 파일 생성
          파일의 날짜와 시간을 수정
touch 파일명 : 파일명의 파일을 생성
touch -c filname : filename의 시간을 현재 시간으로 갱신
touch -ㅅ 20221110142038 filename : filename의 시간을 날짜정보(YYYYMMDDhhmm)로 갱신
touch -r oldfile newfile : newfile의 날짜 정보를 oldfile의 날짜와 동일하게 변경


4. mkdir (make directory) : 디렉터리 생성
nmkdir dirname : dirname이라는 디렉터리 생성
nmkdir dir1 dir2 : 한 번에 여러 디렉터리 생성
nmkdir -p dirname/sub_dirname : dirname 생성
                  sub_dirname 하위 디렉터리 생성
nmkdir -m 700 dirname : 특정 퍼미션(권한)을 갖는 디렉터리


8진수   2진수     권한 의미
0    000 --- 아무 권한 없음
1    001 --x 실행 권한만 있음
2    010 -w- 쓰기 권한만 있음
3    011 -wx 쓰기, 실행 권한 있음
4    100 r-- 읽기 권한만 있음
5    101 r-x 읽기,실행 권한 있음
6    110 rw- 읽기,쓰기 권한 있음
7    111 rwx 모든 권한 있음

예를 들어 '777'의 경우 이진수로 111111111이고
rwxrwxrwx라는 의미를 가지므로 파일 소유자,
소유 그룹, 일반 사용자에게 읽기, 쓰기, 실행의
모든 권한을 주는 설정이다.


5. cp (Copy) : 파일 복사
cp file1 file2 : file1을 file2 라는 이름으로 복사
cp -f file1 file2 : 강제 복사(file2 라는 파일이 이미 있울 경유 강제로 기존 file2를 지우고 복사)
cp -r dir1 dir2 : 디렉터리 복사. 폴더안의 모든 하위 경로와 파일들을 복사

6. mv (Move) : 파일 이동
mv file1 file2 : file1 파일을 file2 파일로 변경
mv file1 /dir : file1 파일을 dir 디렉터리로 이동
mv file1 file2 /dir : 여러 파일 dir 디렉터리로 이동
mv /dir /dir2 : dir1 디렉터리를 dir2 디렉터리로 이름 변경


7. rm (Remove) : 파일 삭제
rm file1 : file1 을 삭제
rm -f file1 : file1 을 강제 삭제
rm -r dir : dir 디렉터리 삭제 (디렉터리는 -r 옵션 없이 삭제 불가)


8. cat(Catenate) : 파일의 내용을 화면에 출력, 리아이렉션 기호('>')룰 사용하여 새로운 파일을 생성
cat file1 : file1의 내용을 출력
cat file1 file2 : file1 과 file2 의 내용을 출력
cat file1 file2 | more : file1 과 file2 의 내용을 페이지별로 출력
cat file1 file2 | head : file1 과 file2 의 내용을 처음부터 10번째 줄까지만 출력
cat file1 file2 | tail : file 과 file2 의 내용을 끝에서 10번쨰 줄까지만 출력


9. redirection ('>', '>>') : 화면의 출력 결과를 파일로 저장
'>' 기호 : 기존에 있는 파일 내용을 지우고 저장
'>>' 기호 : 기존 파일 내용 뒤에 덧 붙여서 저장
'<' 기호 : 파일의 데이터를 명령에 입력

10. head, tail - 파일 위(head) 아래(tail) 출력
'''