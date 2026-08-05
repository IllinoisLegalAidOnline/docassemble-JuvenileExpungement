from docassemble.base.util import today

def is_eligible(arrest):
  if arrest.after_arrest == "court" and arrest.at_court == "other":
    if arrest.found_guilty == "other" or arrest.found_guilty == "traffic" or arrest.found_guilty == "murder":
      return False
    elif arrest.found_guilty == "felony_or_a" and (arrest.must_register or not arrest.has_ended or arrest.case_end_date > today().minus(years=2)):
      return False
  elif (arrest.after_arrest == "successful_supervision" or arrest.after_arrest == "failed_supervision") and arrest.must_register:
    return False
  return True