# Instruction
This challenge splits is organised into three phases: (i) implementation of some cryptographic protocols, and then running of (ii) black-box, and (iii) white-box attacks to break other teams’ work.
## Phase 1
The goal of the first phase is to implement some ciphers with respect to the following rules.
* At least two different ciphers must be implemented
* At least one the two ciphers must be new knowledge, that is not have been mentioned in the lecture
or assignments
* Each implementation must be clearly documented (i.e. accompanied by a detailed README file and provide links to the description of ciphers that have not been studied in the course)
* The implementation should include at least three functions: `generate`, `encrypt`, and `decrypt`, which should generate a random set of parameters, encrypt a given plaintext, and decrypt a given
ciphertext, respectively. * Chose a ciphertext, generated from a **meaningful plaintext**, that will have to be broken for each implementation
* The program should be written in C or C++
* The implementations as well as the ciphertexts to be broken must be posted on Sakai before July 3rd, 23:59
* For each cipher pack the source code as well as a Makefile and a README file in a tar archive
* Adjust the Makefile in order for the binary to be compiled into a file called c2
* The program should read the input from the command line arguments and output on the standard output (screen)
* The following arguments should be implemented:
    * `--generate`: generate generate a key
    * `--encrypt`: encrypt a message
    * `--decrypt`: decrypt a message
    * `--key`: use the specified key to encrypt or decrypt
* The set of symbols for the message, the key, and the ciphertext should not include any element not in the alphabet `{a-zA-Z0-9,.;?!()}`
#### Example
```
$ ./c2 --encrypt "mysecretmessage" --key "mysecretkey"
myencryptedmessage
```
## Phase 2

For two weeks starting July 4th every team will be able to run blackbox attacks in order to break each other’s encryption schemes. The goal is to recover the plaintexts corresponding to the ciphertexts. In this second phase the attacks will be run through a website whose address will be provided. The process is as follows:
* Log onto the website
* Select the cipher you desire to attack
* Select the type of attack to run

## Phase 3

On July 18th, all the source codes of the still unbroken ciphers will be uploaded on Sakai. Any kind of attack will then be allowed, including for instance side-channel attacks.

## Phase 4
For each implementation, the ciphertext to break should be rated with a number of credits to be won when its corresponding plaintext is recovered. The total credits for all the implementations of a team should be 10. If the secret key is also recovered using a cryptographic attack a bonus of +2 credits will be awarded.

If the winning team is composed of more than one student it will get a +10 bonus, to be shared among all the team members, on their final grade. The second +8, the third +6, and all the other participating teams +3 marks. If the winning team is composed of a single student the bonus will be set to +5, +3, or +2 depending if the student finishes first, second, or third, respectively. The participation bonus is worth +1 mark.

The final score is calculated as follows:
* The initial score is 0 for all the team.
* When a team recovers a plaintext during phase 2 it gets twice its corresponding credits.
* When a team recovers a plaintext during phase 3 it gets its corresponding credits.
* The team who created the broken ciphertext loses a number of credits equal to the credits awarded
to the other teams.
* At the end, all the scores are calculated and the teams are ordered in increasing order with respect
to their final score. In case of a tie, groups are ordered with respect to the number of plaintext
they recovered and if this is still a tie the number of their plaintext recovered by other teams is
considered.

## Phase 5
Please read carefully those final comments.
* Cheating by providing other teams with an incomplete code (e.g. removing a function) or a code that does not compile will result in being removed from the challenge competition
* It is not allowed to obscure the code by adding useless computation or express simple things in a complex manner
* Following Kerckhoff’s principle everything must be known from the attacking teams, except the secret key
* If a team does not follow Kerckhoff’s principle, **each missing information** will result in a **-2 penalty** on its final score for the challenge
* If the two chosen schemes have already been implemented in the course no reward will be awarded, not even the participation bonus
* Feel free to contact other groups if you have questions
* In case of conflict please contact the teaching team as early as possible