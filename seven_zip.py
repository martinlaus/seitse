import os
import sys
import shutil
import platform
from subprocess import call


class SevenZip:

    def create_archive_with(self, name, files):
        print(name, files)
        for file in files:
            print(file)
            archive_command = ['7za', 'a', '-t7z', name, file]
            call(archive_command)


    def extract_archive(self, archive, destination=None, default_dir='binary'):
        """Extract archive (extracts 7z archives)

        @param archive: path to archive
        @param destination: where to extract

        @return: destination folder
        """
        if not destination:
            destination = os.path.join(os.path.dirname(archive), default_dir)
        print('Extracting archive. Params: %s', locals())

        try:
            if archive.endswith('.7z'):
                if sys.platform == 'darwin':
                    extract_seven_zip = ['7za', 'x', archive, '-o{0}'.format(destination)]
                if 'linux' in sys.platform:
                    extract_seven_zip = ['7za', 'x', archive, '-o{0}'.format(destination)]
                if sys.platform == 'win32':
                    extract_seven_zip = ['7z', 'x', archive, '-o{0}'.format(destination)]
                print('Platform: {0} detected'.format(sys.platform))
                call(extract_seven_zip)
        except:
            print('Unable to extract archive')

            if not os.path.isdir(destination):
                os.makedirs(destination)
            try:
                print('Trying to copy %s to %s', archive, destination)
                shutil.copy2(archive, destination)
            except:
                print('Failed to copy archive')
            
            return os.path.join(destination, os.path.basename(archive))

        return destination