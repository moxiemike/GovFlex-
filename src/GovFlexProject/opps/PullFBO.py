'''
  filename: PullFBO.py
  author:   Jake Lewandosky
  company:  55B Labs
  project:  GovFlex
  date:     05/28/19
  
  brief: Pulls FBO data from their database recover URL. There is also the
         ability to use a dataframe object and verify attribute entries of
         the whole dataframe.
'''


'''
  brief:  Given a string, scrub the date out of the string.
  
  input:  Date string to get date from. (string)
  
  output: Date time object from the string or None. (DateTime)
'''
def ScrubDate(dateString):
  from datetime import datetime as dt
  import pandas as pd
  dateFmt = '%Y-%m-%d' # used only for date collection
  
  if pd.isnull(dateString) or dateString == '':
    dateString = None
  else:
    dateString = dateString.split()
    dateString = dt.strptime(dateString[0], dateFmt)
    
  return dateString
################################################################################

'''
  brief:  Ensures FBO data is up to date and will directly pull from the FBO
          recovery URL with the latest entry specified.
  
  input:  None (void)
  
  output: None (void)
'''
def PullFBOdata():
  from datetime import datetime as dt
  import pandas as pd
  from ftplib import FTP
  from pathlib import Path
  from .models import Opportunity
  
## TODO: set this up to be used with an a daemon
  # get the previous Saturday
  now = dt.today()
  Saturday = 6
  if now.weekday() != Saturday:
    Saturday = now.day - now.isoweekday() - 1 # store previous Saturday
  
  # download file string
  FBOfilename = 'FBORecovery%d%02d%d.csv' % (now.year, now.month, Saturday)
  # storing file string with path
  filepath = 'db/' + FBOfilename
  # download FBO backup opportunity database using FTP
  url = 'ftp.fbo.gov'
  
  FBO = FTP(url)
  FBO.login() # use default login
  
  config = Path(filepath)  
  # only download if the file is not on drive
  if not config.is_file():
    # open a local file to store on disk as binary
    FBOcsv = open(filepath, 'wb')
    FBO.retrbinary('RETR /FBORecovery/' + FBOfilename, FBOcsv.write, 1024)
    FBOcsv.close()
    
    # shutdown the FTP connection and the file
    FBO.quit()
    FBO.close()
  
  # read in as a database
  # cols = ['Title', 'Sol #', 'Agency', 'Office', 'Location', 'Type', 'Orig. Type',
  #         'Last Posting Date', 'Orig. Posting Date', 'Response Deadline',
  #         'Archiving Policy', 'Archive Date', 'Set-aside Type', 'Classification Code',
  #         'Naics Code', 'Office Address', 'Contact Info', 'Place of Performance',
  #         'Description', 'Additional Info Link', 'Active', 'Link']
  
  FBOdf = pd.read_csv(filepath, encoding='ISO-8859-1', nrows=10)
  size = int(FBOdf.size / len(FBOdf.columns))
  
  for i in range(0, size):
    # scrub inputs
    lPost = ScrubDate(FBOdf.at[i,'Last Posting Date'])
    orgPost = ScrubDate(FBOdf.at[i,'Orig. Posting Date'])
    arcDate = ScrubDate(FBOdf.at[i,'Archive Date'])
    
    newOpp = Opportunity(title=FBOdf.at[i, 'Title'],
                         solicNum=FBOdf.at[i, 'Sol #'],
                         agency=FBOdf.at[i,'Agency'],
                         office=FBOdf.at[i,'Office'],
                         location=FBOdf.at[i,'Location'],
                         jobType=FBOdf.at[i,'Type'],
                         origJobType=FBOdf.at[i,'Orig. Type'],
                         lastPost=lPost,
                         origPost=orgPost,
                         respDeadline=FBOdf.at[i,'Response Deadline'],
                         archPolicy=FBOdf.at[i,'Archiving Policy'],
                         archDate=arcDate,
                         setAsideType=FBOdf.at[i,'Set-aside Type'],
                         classCode=FBOdf.at[i,'Classification Code'],
                         NAICScode=FBOdf.at[i,'Naics Code'],
                         officeAddr=FBOdf.at[i,'Office Address'],
                         contactInfo=FBOdf.at[i,'Contact Info'],
                         placeOfPerf=FBOdf.at[i,'Place of Performance'],
                         description=FBOdf.at[i,'Description'],
                         addInfoLink=FBOdf.at[i,'Additional Info Link'],
                         active=FBOdf.at[i,'Active'],
                         link=FBOdf.at[i,'Link']
                         )
    newOpp.save()
## ENDTODO
################################################################################


'''
  brief:  Given a column to look up in a pandas dataframe, look through each
          entry of the 
  
  input:  col   - name of an attribute in the dataframe (string)
          FBOdf - dataframe of FBO data pulled from the recovery URL (panadas
                  dataframe object)
  
  output: None (void)
'''
def VerifyAttribute(col, FBOdf):
    uniques = set()
    blank = False
    
    # look at each entry in dataframe
    for i in range(FBOdf.size):
      data = FBOdf.at[i, col]
      
      # look for blanks and scan length
      if not blank and (data is None or data == '' or pd.isnull(data)):
        blank = True
        print('Blanks in data column %s' % col)
      # entry is not blank
      elif (data is not None or data != '' or not pd.isnull(data)):
        # measure the entry and store if it is the longest entry of attribute
        if len(str(data)) > longest:
          longest = len(str(data))
          uniques.add(data)
      
    # print if there aren't any blanks in column
    if not blank:
      print('No blanks found in column: %s.' % col)
    # print if any non-unique values exist
    if len(uniques) < FBOdf.size - 1:
      print('Non-unique values found in column %s.' % col)
    # print length of longest entry in column
    print('Longest value found in column %s: %d\n' % (col, longest))
################################################################################