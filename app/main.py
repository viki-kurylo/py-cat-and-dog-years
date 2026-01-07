def get_human_age(cat_age: int, dog_age: int) -> list:

    cat_first_year_gap = 15
    cat_second_year_gap = 9 + cat_first_year_gap
    cat_other_years_gap = 4

    if cat_age < cat_first_year_gap:
        cat_human_years = 0
    elif cat_age < cat_second_year_gap:
        cat_human_years = 1
    elif cat_age < cat_second_year_gap + cat_other_years_gap:
        cat_human_years = 2
    else:
        cat_human_years = ((cat_age - cat_second_year_gap)
                           // cat_other_years_gap + 2)

    dog_first_year_gap = 15
    dog_second_year_gap = 9 + dog_first_year_gap
    dog_other_years_gap = 5

    if dog_age < dog_first_year_gap:
        dog_human_years = 0
    elif dog_age < dog_second_year_gap:
        dog_human_years = 1
    elif dog_age < dog_second_year_gap + dog_other_years_gap:
        dog_human_years = 2
    else:
        dog_human_years = ((dog_age - dog_second_year_gap)
                           // dog_other_years_gap + 2)

    return [cat_human_years, dog_human_years]
