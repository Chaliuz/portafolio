from ranger import MAX_RESTORABLE_TABS
from ranger.api.commands import Command
from plugins.ranger_udisk_menu.mounter import mount

class paste_as_root(Command):
	def execute(self):
		if self.fm.do_cut:
			self.fm.execute_console('shell sudo mv %c .')
		else:
			self.fm.execute_console('shell sudo cp -r %c .')

class fzf_select(Command):
    """
    :fzf_select

    Find a file using fzf.

    With a prefix argument select only directories.

    See: https://github.com/junegunn/fzf
    """
    def execute(self):
        import subprocess
        import os.path
        if self.quantifier:
            # match only directories
            command="find -L . \( -path '*/\.*' -o -fstype 'dev' -o -fstype 'proc' \) -prune \
            -o -type d -print 2> /dev/null | sed 1d | cut -b3- | fzf +m --reverse --header='Jump to file'"
        else:
            # match files and directories
            command="find -L . \( -path '*/\.*' -o -fstype 'dev' -o -fstype 'proc' \) -prune \
            -o -print 2> /dev/null | sed 1d | cut -b3- | fzf +m --reverse --header='Jump to filemap <C-f> fzf_select'"
        fzf = self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)
        stdout, stderr = fzf.communicate()
        if fzf.returncode == 0:
            fzf_file = os.path.abspath(stdout.rstrip('\n'))
            if os.path.isdir(fzf_file):
                self.fm.cd(fzf_file)
            else:
                self.fm.select_file(fzf_file)

import os
from ranger.core.loader import CommandLoader
class extract_here(Command):
    def execute(self):
        """ extract selected files to current directory."""
        cwd = self.fm.thisdir
        marked_files = tuple(cwd.get_selection())

        def refresh(_):
            cwd = self.fm.get_directory(original_path)
            cwd.load_content()

        one_file = marked_files[0]
        cwd = self.fm.thisdir
        original_path = cwd.path
        au_flags = ['-x', cwd.path]
        au_flags += self.line.split()[1:]
        au_flags += ['-e']

        self.fm.copy_buffer.clear()
        self.fm.cut_buffer = False
        if len(marked_files) == 1:
            descr = "extracting: " + os.path.basename(one_file.path)
        else:
            descr = "extracting files from: " + os.path.basename(
                one_file.dirname)
        obj = CommandLoader(args=['aunpack'] + au_flags
                            + [f.path for f in marked_files], descr=descr,
                            read=True)

        obj.signal_bind('after', refresh)
        self.fm.loader.add(obj)


# Chalius commands:
class extract_audio(Command):
    """
    :extract_audio

    Extract audio from current video file with ffmpeg.
    """
    def execute(self):
        import subprocess
        this_file = self.fm.thisfile
        command="ffmpeg -i "+ this_file.path +" -acodec libmp3lame audio.mp3"

        self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)

class flip_horizontally_old(Command):
    """
    :flip_horizontally

    Flip current video horizontally.
    """
    def execute(self):
        import subprocess
        this_file = self.fm.thisfile
        command="ffmpeg -i " + this_file.path + "  -vf hflip -c:a copy flipped.mp4"

        self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)

class flip_horizontally(Command):
    """
    :flip_horizontally2

    Flip current video horizontally2.
    """
    def execute(self):
        import subprocess
        this_file = self.fm.thisfile
        # OLD:
        # ---------------------------------------------------
        # command="ffmpeg -i " + this_file.path + "  -vf hflip -c:a copy "+ this_file.path+"_flipped.mp4"
        # command=f"ffmpeg -i {this_file.path} -vf hflip -c:a copy {this_file.basename_without_extension}_flipped.mp4 && rm {this_file.path}"
        # command=f"echo {self.fm.thistab.get_selection}"
        # ---------------------------------------------------

        for item in self.fm.thistab.get_selection(): 
            # item = /home/chalius/projects/videos/fight-videos-project/videos_created/original_videos/temp/Do_It_-Topstreetfights.com_flipped.mp4

            # Extracting basenam without extension:
            basename = item.path[item.path.rfind("/")+1:]
            without_extension = basename[:basename.rfind(".")]
            # ---------------------------------------------------
            command=f"ffmpeg -i {item.path} -vf hflip -c:a copy {without_extension}_flipped.mp4 && rm {item.path}"
            self.fm.run(command)
            # self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)
        

from pymediainfo import MediaInfo
def get_times(path):
    media_info = MediaInfo.parse(path)
    times_array = []
    for track in media_info.tracks:
        if track.track_type == "Video":
            seconds = track.duration / 1000
            time1 = round(seconds * 0.1)
            time2 = round(seconds * 0.3)
            time3 = round(seconds * 0.7)
            time4 = round(seconds * 0.9)
            times_array = [time1, time2, time3, time4]
            return times_array
        elif track.track_type == "Audio":
            print("Track data:")
            # pprint(track.to_data())
            raise Exception("File path isn't a video.")
    return times_array

def make_one_screenshot(seconds, path, output):
    '''Create the screenshot.'''
    # Example:
    # cmd = f"ffmpeg -ss 10 -i {path} -frames 1 screenshot.png"
    cmd = f"ffmpeg -ss {seconds} -i {path} -frames 1 {output}"
    os.system(cmd)

from PIL import Image, ImageEnhance
def make_collage(images_array, output_folder, video_name):
    print(images_array)
    print(output_folder)
    print(video_name)

    # images_array:
    # ['./functions/screenshot/temp/4.png', './functions/screenshot/temp/11.png', './functions/screenshot/temp/26.png', './functions/screenshot/temp/34.png']

    new_image = Image.new("RGBA", (2000,2000))

    # img = Image.open("Desktop/300.jpg")
    img1 = Image.open(images_array[0])
    img2 = Image.open(images_array[1])
    img3 = Image.open(images_array[2])
    img4 = Image.open(images_array[3])

    img1 = img1.resize((1000,1000))
    img2 = img2.resize((1000,1000))
    img3 = img3.resize((1000,1000))
    img4 = img4.resize((1000,1000))

    new_image.paste(img1, (0,0))
    new_image.paste(img2, (1000,0))
    new_image.paste(img3, (0,1000))
    new_image.paste(img4, (1000,1000))

    # new.show()
    # output = new_image.save("./output.png")
    output = new_image.save(f"{output_folder}{video_name}.png")

import shutil
class make_screenshots(Command):
    """
    :make_screenshots

    This command makes screenshots of the videos from the current folder.
    """
    def execute(self):
        for item in self.fm.thistab.get_selection(): 
            video_path = item.path

            # Take pictures:
            # ---------------------------------------------------
            times = get_times(video_path)
            images_array = []

            # temp_folder = "./functions/screenshot/temp/"
            temp_folder = f"{item.dirname}/temp/"
            if not os.path.exists(temp_folder): os.makedirs(temp_folder)

            for time in times:
                # temp_output = f"./screenshots/temp/{time}.png"
                temp_output = f"{temp_folder}{time}.png"
                make_one_screenshot(time, video_path, temp_output)
                images_array.append(temp_output)

            # ---------------------------------------------------

            # Make collage:
            # ---------------------------------------------------
            # Extract name from video_path
            arr_path = video_path.split("/")
            video_name = arr_path[len(arr_path)-1]
            # ------------------------

            out_folder = "./output/"
            collages_folder = out_folder
            if not os.path.exists(collages_folder): os.makedirs(collages_folder)
            make_collage(images_array, collages_folder, video_name)

            shutil.rmtree(temp_folder)
            # ---------------------------------------------------


class test(Command):
    """
    :test

    Test command.
    """
    def execute(self):
        import subprocess
        # this_file = self.fm.thisfile
        command=f"echo {Command}"

        self.fm.execute_command(command, universal_newlines=True, stdout=subprocess.PIPE)