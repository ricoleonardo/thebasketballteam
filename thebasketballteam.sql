CREATE TABLE `country` (
  `id` integer PRIMARY KEY,
  `country` varchar(255)
);

CREATE TABLE `city` (
  `id` integer PRIMARY KEY,
  `city` varchar(255),
  `country` [id]
);

CREATE TABLE `teams` (
  `id` integer PRIMARY KEY,
  `name` [id],
  `city` [id]
);

CREATE TABLE `coaches` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `teams` [id],
  `country` [id]
);

CREATE TABLE `players` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `teams` [id]
);

CREATE TABLE `coach_types` (
  `id` integer PRIMARY KEY,
  `type` varchar(255)
);

CREATE TABLE `games` (
  `id` integer PRIMARY KEY,
  `seasons` [id],
  `home` [id],
  `visitor` [id]
);

CREATE TABLE `seasons` (
  `id` integer PRIMARY KEY,
  `seasons` integer
);

ALTER TABLE `city` ADD FOREIGN KEY (`country`) REFERENCES `country` (`id`);

ALTER TABLE `teams` ADD FOREIGN KEY (`city`) REFERENCES `city` (`id`);

ALTER TABLE `games` ADD FOREIGN KEY (`home`) REFERENCES `city` (`id`);

ALTER TABLE `players` ADD FOREIGN KEY (`teams`) REFERENCES `teams` (`id`);

ALTER TABLE `games` ADD FOREIGN KEY (`visitor`) REFERENCES `teams` (`id`);

ALTER TABLE `coaches` ADD FOREIGN KEY (`teams`) REFERENCES `teams` (`id`);

ALTER TABLE `coach_types` ADD FOREIGN KEY (`id`) REFERENCES `coaches` (`id`);

ALTER TABLE `games` ADD FOREIGN KEY (`seasons`) REFERENCES `seasons` (`id`);
