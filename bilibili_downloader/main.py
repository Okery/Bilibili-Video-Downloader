import argparse
from downloader import BiliDownloader
from multiprocessing import cpu_count

# ---------------下载路径 & Cookie-----------------
DIRNAME = 'E:/downloads'
COOKIE = 'SESSDATA=3f5681db%2C1702651790%2C8c420*41'
# --------------------------------------------------


def main(args):
    bili_downloader = BiliDownloader(args.url, args.dir_name, args.cookie, args.max_workers)
    bili_downloader(args.page, args.quality, args.mode)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', type=str)
    parser.add_argument('--page', '-p', type=int, nargs='+', default=1)
    parser.add_argument('--quality', '-q', type=int, default=3)
    parser.add_argument('--mode', type=str, default='common')
    parser.add_argument('--dir-name', type=str, help='absolute path to save videos')
    parser.add_argument('--cookie', type=str, help='VIP COOKIE is better. Update it once a month ')
    parser.add_argument('--max-workers', type=int)
    args = parser.parse_args()

    args.dir_name = DIRNAME
    args.cookie = COOKIE
    args.max_workers = cpu_count() // 2
    
    main(args)
