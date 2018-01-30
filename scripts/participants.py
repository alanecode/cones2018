#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to generate json data about speakers and delegates.

Edit main to separate input data into subsets for 'speakers' and 'delegates',
creating a dataframe for each. Create a ParticipantDataset for each and use its
to_json() method to create appropriately formatted json in the ../public/data/
directory.
"""
import pandas as pd

class ParticipantDataset(object):
    """Formats received participant data into a standardised json format."""

    def __init__(self, df, role, first_name_col, surname_col, title_col,
            institution_col=None, homepage_col=None, twitter_col=None):
        """Construct ParticipantDataset object.

        Params:
            df : pandas.DataFrame
                DataFrame containing source data for display on speakers/
                attendants pages.

            role : str
                Must be one of 'speakers' or 'attendants', specifying
                whether we are generating data for the speakers or
                attendants page of the website.

            first_name_col : str
                Name of the column in df where speaker first name is stored

            surname_col : str
                Name of the column in df where speaker surname is stored

            title_col : str
                Name of the column in df where speaker's title is stored,
                e.g 'Dr', or 'Prof'

            homepage_col : str, default None
                Name of the column in df where speaker homepages are stored,
                if given

            twitter_col : str, detault None
                Name of the column in df where speaker twitter handles are
                stored, if given
        """

        self.role = role
        self.first_name_col = first_name_col
        self.surname_col = surname_col
        self.title_col = title_col
        self.institution_col = institution_col
        self.homepage_col = homepage_col
        self.twitter_col = twitter_col
        self.df = self._proc_df(df)

    def _proc_df(self, df):
        """Do some basic data integrity checks on received DataFrame."""
        # check specified columns do actually exist in the DataFrame
        for c in [self.first_name_col, self.surname_col,
                  self.title_col]:
            if c not in df.columns:
                raise ValueError('Given column name "'+str(c)+'" not in '\
                        'DataFrame.')

        for c in [self.role, self.first_name_col, self.surname_col,
            self.title_col]:
            if not isinstance(c, str):
                raise TypeError(str(c)+' must be a string.')

        if self.role not in ['speakers', 'attendants']:
            raise ValueError('Role must be specified as either "speaker" '\
                'or "attendant"')

        df = df.rename(columns = {self.first_name_col:'forename',
                                  self.surname_col:'surname',
                                  self.title_col:'title',
                                 })

        if self.institution_col:
            df['institution'] = df[self.institution_col]
            df.drop(self.institution_col, axis=1)
        else:
            df['institution'] = None

        if self.homepage_col:
            df['homepage'] = df[self.homepage_col]
            df.drop(self.homepage_col, axis=1)
        else:
            df['homepage'] = None

        if self.twitter_col:
            df['twitter'] = df[self.twitter_col]
            df.drop(self.twitter_col, axis=1)
        else:
            df['twitter'] = None


        return df[['title', 'forename', 'surname', 'institution', 'twitter',
            'homepage']]

    def to_json(self):
        fname = '../public/data/'+self.role+'.json'
        self.df.to_json(fname, orient='records')

class SpeakerDataset(ParticipantDataset):
        def __init__(self, df, first_name_col, surname_col, title_col,
            institution_col=None, homepage_col=None, twitter_col=None,
            talk_title_col=None, plenary_col=None):
            self.all_df = df.copy()
            super().__init__(df, 'speakers', first_name_col, surname_col,
                title_col, institution_col, homepage_col, twitter_col)

            self.talk_title_col = talk_title_col
            self.plenary_col = plenary_col
            self.df = self._proc_all_df()
            del self.all_df

            #print(self.df.head())
            #print(self.all_df.head())
        def _proc_all_df(self):
            """Add in speaker specific data to the already processed DataFrame."""
            self.df['talkTitle'] = self.all_df[self.talk_title_col]
            self.df['plenarySession'] = self.all_df[self.plenary_col]

            return self.df

if __name__ == '__main__':
    all_dat = pd.read_csv('../data-src/participant_data.csv')
    speakers = all_dat[all_dat.role=='speaker']
    attendants = all_dat[all_dat.role=='delegate']

    speakers = SpeakerDataset(speakers, 'first_name', 'surname',
        'title', institution_col='university', homepage_col='homepage',
        twitter_col='twitter', talk_title_col='talk_title',
        plenary_col='plenary')

    attendants = ParticipantDataset(attendants, 'attendants', 'first_name',
        'surname', 'title', homepage_col='homepage', twitter_col='twitter')

    speakers.to_json()
    attendants.to_json()
