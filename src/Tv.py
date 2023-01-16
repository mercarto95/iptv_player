import _parser_

class Tv:
    def __init__(self, tv_name) -> None:
        # read local tv file contents from HD
        file_content = _parser_.read_tvFile_contents(tv_name)
        # parse the file contents       
        if file_content == False:
            self.is_loaded = False 
        else:
            self.is_loaded = True 
            _parser_.parse_file_contents(file_content)
            # get channels 
            self.channels = _parser_.get_channels()
            self.movies = _parser_.get_movies()
            self.series = _parser_.get_series()


