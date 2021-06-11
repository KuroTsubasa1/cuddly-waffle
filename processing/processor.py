
class Processor:

    def get_infections_by_gender_by_date(self, data):
        gender_data = data['Geschlecht'].value_counts()
        return gender_data


