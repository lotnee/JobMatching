import csv
import random

def generate_csv(filename, num_rows):
    skills = ['Python', 'Java', 'JavaScript', 'C++', 'SQL', 'HTML/CSS', 'React', 'Node.js', 'Ruby', 'PHP']
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'skills']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for i in range(1, num_rows + 1):
            num_skills = random.randint(1, 3)  # Randomly choose 1 to 3 skills per person
            person_skills = random.sample(skills, num_skills)  # Randomly select skills
            skill_string = ', '.join(person_skills)  # Join skills into a CSV string
            
            writer.writerow({
                'id': i,
                'name': f'Person {i}',
                'skills': skill_string
            })

# Example usage:
filename = 'thousands.csv'
num_rows = 1000000
generate_csv(filename, num_rows)
print(f"CSV file '{filename}' generated with {num_rows} rows.")