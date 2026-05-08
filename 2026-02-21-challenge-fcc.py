""""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on, February, 21rst, 2026.

----------------------------
2026 Winter Games Day 16: Curling
Given a 5x5 matrix representing the "house" at the end of a curling round, 
determine which team scores and how many points they score.

The layout:

The center cell (index [2, 2]) is the "button".
The 8 cells directly surrounding the button represent ring 1.
And the 16 cells on the outer edge of the house represent ring 2.

-- In the given matrix:

"." represents an empty space.
"R" represents a space with a red stone.
"Y" represents a space with a yellow stone.

-- Scoring rules:

- Only one team can score per round.
- The team with the stone closest to the button scores.
- The scoring team earns 1 point for each of their stones 
that is closer to the button than the opponent's closest stone.
- The lower the ring number, the closer to the center the stone is.
- If both teams' closest stone is the same distance from the center, no team scores.

Return:

A string in the format "team: number_of_points". e.g: "R: 2".
or "No points awarded" if neither team scored any points.

For example, given:

[
  [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."],
  ["Y", ".", ".", ".", "."],
  [".", "R", ".", ".", "."],
  [".", ".", ".", ".", "."]
]

Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows closest.

Tests:
1. score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]]) should return "R:2".
2. score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]]) should return "Y: 3".
3. score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]]) should return "No points awarded".
4. score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]]) should return "R: 4".
5. score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]]) should return "Y: 1".
6. score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]]) should return "No points awarded".
"""

def score_curling(house):
    # Remember house is a matrix 5x5
    # Important positions
    button = house[2, 2]

  # As the postions of the inner ring are contants 
    inner_ring = ((2, 1), (1, 1), (1, 2), 
                  (1,3), (3, 1), (3, 2),
                    (3, 3), (2, 3))
    
    outer_ring = ((0, 0), (0,1), (0,2), (0,3), (0, 4),
                  (1, 0), (1, 4),
                  (2, 0), (2, 4),
                  (3, 0), (3,4),
                  (4, 4), (4,1), (4,2), (4,3), (4, 4))

    # Checking to see if we already have a tie
    inner_ring_analysis = evaluate_inner_ring(house, inner_ring)

    if inner_ring_analysis == 'TIE':
        result = 'No points awarded'
        print(result)
        return result
    
    if button != '.' and inner_ring_analysis['team'] == button:
        inner_ring_analysis['score'] += 1

    else:
        print(f'The team {button} won with 1 point!')

    # If the other team hasn't won, we now evaluate the outer ring 

    
    return house




def evaluate_inner_ring(house, inner_ring):
    scoring_team = ''
    scoring_team_points = 0

    # Using matrix syntax (m for rows and n  for columns)
    for index, (m, n) in enumerate(inner_ring):
        element_being_evaluated = house[m,n]
        
        if house[m,n] != ".":
            print(f'Team scoring, {element_being_evaluated}')

            # Checking if is the first team to score
            if scoring_team == '':  
                scoring_team = element_being_evaluated

            # Checking if is the same team scoring or is a different one
            if scoring_team != element_being_evaluated:
                result = "TIE"
                print(result)
                return result
            
            # As the previous if wasn't activated
            scoring_team_points += 1
    

    scoring = { 'team': scoring_team, 'score': scoring_team_points}
    print(f'The current scoring is {scoring}')
    return scoring




def evaluate_outer_ring(house, outer_ring, team_scoring, current_score):
    scoring_team = team_scoring
    scoring_team_points = 0
    points_to_be_added = 0

    # Using matrix syntax (m for rows and n  for columns)
    for index, (m, n) in enumerate(outer_ring):
        element_being_evaluated = house[m,n]
        
        # If we find other team in the outer ring,, the stones from the winning team doesn't count.
        if element_being_evaluated != scoring_team or element_being_evaluated != '.':
            
            print(f'Different team, stop counting. {element_being_evaluated}')
            print( f'Team scoring {scoring_team} with {scoring_team_points} points')

            result = f'{scoring_team}: {scoring_team_points}'
            print(result)
            return result
        
        elif element_being_evaluated == scoring_team:
            points_to_be_added += 1

    final_score = scoring_team_points + points_to_be_added
    result = f'{scoring_team}: {final_score}'
    print(result)
    return result




# Tests
score_curling([[".", ".", "R", ".", "."], [".", "R", ".", ".", "."], ["Y", ".", ".", ".", "."], [".", "R", ".", ".", "."], [".", ".", ".", ".", "."]])
score_curling([[".", ".", "R", ".", "."], [".", ".", ".", ".", "."], [".", ".", "Y", ".", "R"], [".", ".", "Y", "Y", "."], [".", "Y", "R", "R", "."]])
score_curling([[".", "R", "Y", ".", "."], ["Y", ".", ".", ".", "."], [".", ".", ".", ".", "."], [".", "Y", "R", "Y", "."], [".", ".", "R", "R", "."]])
score_curling([[".", "Y", "Y", ".", "."], ["Y", ".", ".", "R", "."], [".", ".", "R", ".", "."], [".", ".", "R", "R", "."], [".", "Y", "R", "Y", "."]])
score_curling([["Y", "Y", "Y", "Y", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "R", "Y", "R", "Y"], ["Y", "R", "R", "R", "Y"], ["Y", "Y", "Y", "Y", "Y"]])
score_curling([["Y", "R", "Y", "R", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", ".", "Y"], ["R", ".", ".", ".", "R"], ["Y", ".", ".", "R", "Y"]])