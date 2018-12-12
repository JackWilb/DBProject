# Remove all stale memes
rm src/media/MemeGenerator/*.jpg

# Re-load the mysql data in
mysql -u root -p <DBProject.sql

# Build memes
width=`identify -format %w ~/websites/DBProject/src/static/MemeGenerator/sociallyAwkwardPenguin.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Hey, what's up?"  ~/websites/DBProject/src/static/MemeGenerator/sociallyAwkwardPenguin.jpg +swap -gravity north -composite ~/websites/DBProject/src/media/MemeGenerator/temp.jpg
width=`identify -format %w ~/websites/DBProject/src/static/MemeGenerator/sociallyAwkwardPenguin.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Good, you?"  ~/websites/DBProject/src/media/MemeGenerator/temp.jpg +swap -gravity south -composite ~/websites/DBProject/src/media/MemeGenerator/admin1.jpg

width=`identify -format %w ~/websites/DBProject/src/static/MemeGenerator/rickAstley.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Never Gonna Give You Up"  ~/websites/DBProject/src/static/MemeGenerator/rickAstley.jpg +swap -gravity north -composite ~/websites/DBProject/src/media/MemeGenerator/admin2.jpg

width=`identify -format %w ~/websites/DBProject/src/static/MemeGenerator/willyWonka.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"You have finals coming up?"  ~/websites/DBProject/src/static/MemeGenerator/willyWonka.jpg +swap -gravity north -composite ~/websites/DBProject/src/media/MemeGenerator/temp.jpg
width=`identify -format %w ~/websites/DBProject/src/static/MemeGenerator/willyWonka.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:"Tell me about how well your balancing your time"  ~/websites/DBProject/src/media/MemeGenerator/temp.jpg +swap -gravity south -composite ~/websites/DBProject/src/media/MemeGenerator/admin3.jpg

# Output setup complete when images are made
echo "Setup Complete"