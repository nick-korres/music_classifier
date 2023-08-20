from utils.fetch_entries import fetchable_attributes
from utils.attributes import Attributes

exluded_attributes = [Attributes.LABEL,Attributes.FILE_PATH,Attributes.DURATION]

comparable_attributes = [attr.value for attr in fetchable_attributes if attr not in exluded_attributes]